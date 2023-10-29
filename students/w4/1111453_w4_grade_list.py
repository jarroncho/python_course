import openpyxl
from abc import abstractmethod, ABC
import gspread

class Base_Grade_list(ABC):
    @abstractmethod
    def print_data(self):
        pass
    
class Excel_grade_list(Base_Grade_list):
    def __init__(self, file_path: str, data_range: str):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[workbook.sheetnames[0]]
        call_range = sheet[data_range]
        self.data = list()
        for row in sheet[data_range]:
            row_value = list()
            for cell in row:
                row_value.append(cell.value)
            self.data.append(row_value)
        self.__set_sum_and_average()
        self.__set_ranking()
        # print(self.data)
        workbook.close()
    def print_data(self):
        for row in self.data:
            print(row)
    def __set_sum_and_average(self):
        for row in self.data[1:]:
            sum = 0
            for score in row[1:5]:
                sum += score
            row[5] = sum
            row[6] = sum / 4

    def __set_ranking(self):
        rank_dict = dict()
        for i in range(1,len(self.data)):
            rank_dict[i] = self.data[i][5]
        rank_dict = sorted(rank_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        for rank in range(len(rank_dict)):
            self.data[rank_dict[rank][0]][7] = rank+1
print("Excel")
ex = Excel_grade_list("../../teacher/w3/grade_list.xlsx", 'c5:j12')
ex.print_data()

class GS_grade_list(Base_Grade_list):
    def __init__(self, url: str, data_range: str) -> None:  
        gc = gspread.service_account(filename="../../teacher/w4/python_course_access_cred.json")
        sh =gc.open_by_url(url)
        self.data = list(sh.sheet1.get(data_range))
        for i in range(1, len(self.data)):
            for j in range(1, len(self.data[1])):
                self.data[i][j] = eval(self.data[i][j])
        self.__set_sum_and_average()
        self.__set_ranking()

    def print_data(self):
        for row in self.data:
            print(row)
    def __set_sum_and_average(self):
        for row in self.data[1:]:
            sum = 0
            for score in row[1:5]:
                sum += score
            row[5] = sum
            row[6] = sum / 4

    def __set_ranking(self):
        rank_dict = dict()
        for i in range(1,len(self.data)):
            rank_dict[i] = self.data[i][5]
        rank_dict = sorted(rank_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        for rank in range(len(rank_dict)):
            self.data[rank_dict[rank][0]][7] = rank+1

print("Google sheets")
google = GS_grade_list("https://docs.google.com/spreadsheets/d/1nqgiOHVyuIM1p4cBKUsi1HfmkaIhjIQdQYamGbkzOhE/edit#gid=0", 'c5:j12')
google.print_data()