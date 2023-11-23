from abc import ABC, abstractmethod
import gspread
import openpyxl

class grade_list():
    @abstractmethod
    def __int__(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def grade_list(self):
        pass

    @abstractmethod
    def print(self):
        pass
# ===== excel data =====
class excel_data(grade_list):
    def __init__(self, file_data):
        self.file_data = file_data
        self.workbook = openpyxl.load_workbook(file_data)
        self.cell_range_pattern = 'c5:j12'
        self.data_value_2d = []

    def get_data(self):
        self.sheet_names = self.workbook.sheetnames
        self.sheet_name = self.sheet_names[0]
        sheet_name = self.sheet_names[0]
        sheet = self.workbook[sheet_name]
        
        for row in sheet[self.cell_range_pattern]:
            row_values = []  # Create a list for each row
            for cell in row:
                row_values.append(cell.value)
            self.data_value_2d.append(row_values)  # Append the row list to the 2D list

    def grade_list(self):
        #total score
        for i in range(1, len(self.data_value_2d)):
            score = 0
            for j in range(1, 5):
                score += self.data_value_2d[i][j]
            self.data_value_2d[i][5] = score
            self.data_value_2d[i][6] = score / 4
        #rank
        for i in range(1, len(self.data_value_2d)):
            k = 1 
            for j in range (1, len(self.data_value_2d)):
                if(i == j):
                    continue
                else:
                    if(self.data_value_2d[i][5] < self.data_value_2d[j][5]):
                        k += 1
            self.data_value_2d[i][7] = k
        #closs
        self.workbook.close()
    
    def print(self):
        for i in range(len(self.data_value_2d)):
            print(self.data_value_2d[i][0], end='\t')
            for j in range(1, len(self.data_value_2d[i])):
                print(self.data_value_2d[i][j], end='\t')
            print()
        print()

# ===== google sheeet data =====
class gs_data(grade_list):
    def __init__(self, file_data):
        self.file_data = file_data

    def get_data(self):
        gc = gspread.service_account(self.file_data)
        sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1nqgiOHVyuIM1p4cBKUsi1HfmkaIhjIQdQYamGbkzOhE/edit#gid=0')
        cell_range_pattern = 'c5:j12'
        cell_range = sh.sheet1.get(cell_range_pattern)   
        self.grade_list_data = list(cell_range)
    
    def grade_list(self):
        #total score
        length = len(self.grade_list_data[0])
        for i in range(1, length):
            score = 0
            for j in range(1, 5):
                self.grade_list_data[i][j] = int(self.grade_list_data[i][j])
                score += self.grade_list_data[i][j]
            self.grade_list_data[i].append(score)
            average = self.grade_list_data[i][5] / 4
            self.grade_list_data[i].append(average)
        #rank
        for i in range(1, length):
            k = 1 
            for j in range (1, length):
                if(i == j):
                    continue
                else:
                    if(self.grade_list_data[i][5] < self.grade_list_data[j][5]):
                        k += 1
            self.grade_list_data[i].append(k)
    
    def print(self):
        length = len(self.grade_list_data[0])
        for i in range(length):
            print(self.grade_list_data[i][0], end='\t')
            for j in range(1, length):
                print(self.grade_list_data[i][j], end='\t')
            print()
        print()

#testC:\Users\stanley\OneDrive\文件\GitHub\python_course\teacher
excel_test = excel_data('C:/Users/user/Desktop/grade_list.xlsx')
excel_test.get_data()
excel_test.grade_list()
excel_test.print()

googlesheet_test = gs_data('C:/Users/user/Desktop/python_course/teacher/w4/python_course_access_cred.json')
googlesheet_test.get_data()
googlesheet_test.grade_list()
googlesheet_test.print()