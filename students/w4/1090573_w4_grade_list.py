import gspread
import openpyxl
from abc import ABC, abstractmethod

class BaseGradeList(ABC):
    @abstractmethod
    def __init__(self, file_path: str, data_range: str):
        self.file_path = file_path
        self.data_range = data_range
        self.data = []

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def print_data(self):
        pass

class ExcelGradeList(BaseGradeList):
    def __init__(self, file_path: str, data_range: str):
        super().__init__(file_path, data_range)
        self.workbook = None
        self.sheet = None

    def get_data(self):
        self.workbook = openpyxl.load_workbook(self.file_path)
        self.sheet = self.workbook.active
        for row in self.sheet[self.data_range]:
            self.data.append([cell.value for cell in row])
        self.workbook.close()

    def process_data(self):
        rank_dict = {}
        for i, row in enumerate(self.data):
            if i == 0: continue  # Skip header
            total = sum(row[1:5])
            average = total / 4
            row.extend([total, average])
            rank_dict[i] = total
        sorted_rank = sorted(rank_dict.items(), key=lambda item: item[1], reverse=True)
        for rank, (i, _) in enumerate(sorted_rank, start=1):
            self.data[i].append(rank)

    def print_data(self):
        for row in self.data:
            print('	'.join(str(value) for value in row))

class GoogleSheetsGradeList(BaseGradeList):
    def __init__(self, file_path: str, data_range: str):
        super().__init__(file_path, data_range)
        self.gc = None
        self.sh = None

    def get_data(self):
        self.gc = gspread.service_account(filename=self.file_path)
        self.sh = self.gc.open_by_url(self.file_path)  # Assuming the file_path is the URL
        worksheet = self.sh.sheet1
        self.data = worksheet.get(self.data_range)

    def process_data(self):
        rank_dict = {}
        for i, row in enumerate(self.data):
            if i == 0: continue  # Skip header
            total = sum(int(value) for value in row[1:5])
            average = total / 4
            row.extend([total, average])
            rank_dict[i] = total
        sorted_rank = sorted(rank_dict.items(), key=lambda item: item[1], reverse=True)
        for rank, (i, _) in enumerate(sorted_rank, start=1):
            self.data[i].append(rank)

    def print_data(self):
        for row in self.data:
            print('	'.join(str(value) for value in row))

# Example usage:
# excel_list = ExcelGradeList('path_to_excel_file.xlsx', 'A1:E10')
# excel_list.get_data()
# excel_list.process_data()
# excel_list.print_data()

# google_list = GoogleSheetsGradeList('path_to_google_sheets_credentials.json', 'https://docs.google.com/spreadsheets/d/...')
# google_list.get_data()
# google_list.process_data()
# google_list.print_data()