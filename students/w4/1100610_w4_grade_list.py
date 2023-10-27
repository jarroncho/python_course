import gspread
import openpyxl
from pathlib import Path
from abc import ABC, abstractmethod

class Grade_list(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def grade_list(self):
        pass

    @abstractmethod
    def print_list(self):
        pass


class exe_list(Grade_list):
    def __init__(self,excel_file_path):
        self.excel_file_path = excel_file_path
    def get_data(self):
        workbook = openpyxl.load_workbook(self.excel_file_path)
        cell_range_pattern = 'c5:j12'
        sheet_names = workbook.sheetnames
        sheet_name=sheet_names[0]
        sheet = workbook[sheet_name]
        self.cell_values_2d = []
  
        for row in sheet[cell_range_pattern]:
            row_values = []  
            for cell in row:
                row_values.append(cell.value)
            self.cell_values_2d.append(row_values) 
    def grade_list(self):
        for row_values in self.cell_values_2d[0]:
            print(row_values,end='\t')
        print('\n')
        del self.cell_values_2d [ 0 ]
        self.grade_list=self.cell_values_2d
        def sum(x):
            sum1=0
            for i in range(1,5):
                sum1+=int(x[i]);
            return sum1
        x2=[]
        for i in range(len(self.grade_list)):
            x=0
            x=sum(self.grade_list[i])
            self.grade_list[i][5]=x
            self.grade_list[i][6]=x/4
            x2.append(self.grade_list[i][6])
            x2.sort(reverse=True)
        x2.sort(reverse=True)
        for  i in range(len(self.grade_list)):
            self.grade_list[i][7]=x2.index(self.grade_list[i][6])+1
    def print_list(self):
        for i in range(len(self.grade_list)):
            print(self.grade_list[i][0], end='\t')
            for j in range(1, len(self.grade_list[i])):
                print(self.grade_list[i][j], end='\t')
            print()    

class googlesheet(Grade_list):
    def __init__(self,google_file_path):
        self.google_file_path=google_file_path
        
    def get_data(self):
        gc = gspread.service_account(self.google_file_path)
        sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1nqgiOHVyuIM1p4cBKUsi1HfmkaIhjIQdQYamGbkzOhE/edit#gid=0')
        cell_range_pattern='c5:j12'
        cell_range=sh.sheet1.get(cell_range_pattern)
        self.grade_list_data=list(cell_range)
    def grade_list(self):
        for row_values in self.grade_list_data[0]:
            print(row_values,end='\t')
        print('\n')
        del self.grade_list_data [ 0 ]
        self.grade_list=self.grade_list_data
        def sum(x):
            sum1=0
            for i in range(1,5):
                sum1+=int(x[i]);
            return sum1
        x2=[]
        for i in range(len(self.grade_list)):
            x=0
            x=sum(self.grade_list[i])
            self.grade_list[i][5]=x
            self.grade_list[i][6]=x/4
            x2.append(self.grade_list[i][6])
            x2.sort(reverse=True)
        x2.sort(reverse=True)
        for  i in range(len(self.grade_list)):
            self.grade_list[i][7]=x2.index(self.grade_list[i][6])+1
    def print_list(self):
        for i in range(len(self.grade_list)):
            print(self.grade_list[i][0], end='\t')
            for j in range(1, len(self.grade_list[i])):
                print(self.grade_list[i][j], end='\t')
            print()

excel_grade_list=exe_list('C:/Users/stanley/OneDrive/文件/GitHub/python_course/teacher/w3/grade_list.xlsx')
excel_grade_list.get_data()
excel_grade_list.grade_list()
excel_grade_list.print_list()
print("------------------------------------------------------------")
googlesheet_list=googlesheet('C:/Users/stanley/OneDrive/文件/GitHub/python_course/teacher/w4/python_course_access_cred.json')
googlesheet_list.get_data()
googlesheet_list.grade_list()
googlesheet_list.print_list()










