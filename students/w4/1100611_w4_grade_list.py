
import gspread
import openpyxl
from pathlib import Path
from abc import ABC, abstractmethod

class Gradelist(ABC):

    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def get_the_data(self):
        pass

    @abstractmethod
    def calculate_the_data(self):
        pass

    @abstractmethod   
    def show(self):
        pass


class excel(Gradelist):

    def __init__(self,filename):
        self.filename=Path(filename)

    def get_the_data(self):
        workbook = openpyxl.load_workbook(self.filename)
        sheet_names=workbook.sheetnames
        sheet_name=sheet_names[0]
        sheet = workbook[sheet_name]      
        cell_range_pattern='c5:j12'        
        self.cell_values_2d=[]  
        for row in sheet[cell_range_pattern]:
            row_values = []  
            for cell in row:
                    row_values.append(cell.value)
            self.cell_values_2d.append(row_values)

    def calculate_the_data(self):
        row_len=len(self.cell_values_2d)
        for i in range(1,row_len):
                self.cell_values_2d[i][5]=self.cell_values_2d[i][1]+self.cell_values_2d[i][2]+self.cell_values_2d[i][3]+self.cell_values_2d[i][4]
                self.cell_values_2d[i][6]=self.cell_values_2d[i][5]/4
                
        grade_list_sort = sorted(self.cell_values_2d[1:], key=lambda x: x[5])
        for i in range(len(grade_list_sort)):    
            for j in range(1, len(grade_list_sort[i])):
                grade_list_sort[i][7]=i+1

    def show(self):
        print("\n(Excel version) 2D Cell values:")
        for row_values in self.cell_values_2d:
            print(row_values)
        


class googlesheet(Gradelist):
    def __init__(self,filename):
        self.filename=Path(filename)

    def get_the_data(self):
        gc = gspread.service_account(self.filename)
        sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1nqgiOHVyuIM1p4cBKUsi1HfmkaIhjIQdQYamGbkzOhE/edit#gid=0')

        cell_range_pattern='c5:j12'
        cell_range=sh.sheet1.get(cell_range_pattern)   
        self.grade_list_data=list(cell_range)

    def calculate_the_data(self):
        row_len=len(self.grade_list_data[0])
        for i in range(1,row_len):
            self.grade_list_data[i][1]=int(self.grade_list_data[i][1])
            self.grade_list_data[i][2]=int(self.grade_list_data[i][2])
            self.grade_list_data[i][3]=int(self.grade_list_data[i][3])
            self.grade_list_data[i][4]=int(self.grade_list_data[i][4])
            sum=self.grade_list_data[i][1]+self.grade_list_data[i][2]+self.grade_list_data[i][3]+self.grade_list_data[i][4]
            self.grade_list_data[i].append(sum)
            aver=self.grade_list_data[i][5]/4
            self.grade_list_data[i].append(aver)
        grade_list_sort = sorted(self.grade_list_data[1:], key=lambda x: x[5])
        for i in range(len(grade_list_sort)):    
            rank=i+1
            grade_list_sort[i].append(rank)
                
    def show(self):
        print("\n(Google Sheet version) 2D Cell values:")
        for row_values in self.grade_list_data:
            print(row_values)
        

#excel
excel_grade_list=excel('C:\\Users\\Girl\\Desktop\\grade_list.xlsx')
excel_grade_list.get_the_data()
excel_grade_list.calculate_the_data()
excel_grade_list.show()

#googlesheet
googlesheet_grade_list=googlesheet('C:\\Users\\Girl\\Downloads\\pythonw4-90bc51374cbe.json')
googlesheet_grade_list.get_the_data()
googlesheet_grade_list.calculate_the_data()
googlesheet_grade_list.show()
