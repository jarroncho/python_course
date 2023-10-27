from abc import ABC, abstractmethod
import openpyxl
import gspread
class Base_Grade_list(ABC):
    @abstractmethod
    def sum_Calculate(material):
        pass
    def average_Calculate(self):
        pass
    def Ranking(self):
        pass
    def show(self):
        pass
class Excel_grade_list(Base_Grade_list):
     def __init__(self,Excel_sheet):
        self.Excel_sheet=Excel_sheet
     def sum_Calculate(material):
        sums=[]
        for row in cell_range:
            sum=0
            for cell in row:    
                sum+=cell.value
            sums.append(sum)
        return sums    

     def average_Calculate(self):
        arr=self.sum_Calculate()
        list=[x/4 for x in arr]
        return list

     def Ranking(self):
        Ranking_list=[]
        data=self.average_Calculate()
        data_sorted=sorted(data) 
        for i in range(len(data)):
            for j in range(len(data_sorted)):
                if data[i]==data_sorted[j]:
                   Ranking_list.append(len(data)-j)
        return  Ranking_list
     def show(self):
        cell_range_pattern='c5:j12'
        cell_range = sheet[cell_range_pattern]
        for row in cell_range:
            for cell in row:
                print(cell.value, end='\t')  # Print cell value and separate with tabs
            print()  # Move to the next row
class GS_grade_list(Base_Grade_list):
    def __init__(self,path):
        self.path=path
        gc = gspread.service_account(path)
        sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1nqgiOHVyuIM1p4cBKUsi1HfmkaIhjIQdQYamGbkzOhE/edit#gid=0')
        cell_range_pattern='c5:j12'
        cell_range=sh.sheet1.get(cell_range_pattern)
        path= cell_range
    def sum_Calculate(material):
        sums=[]
        for row in cell_range:
            sum=0
            for cell in row:    
                sum+=cell.value
            sums.append(sum)
        return sums    

    def average_Calculate(self):
        arr=self.sum_Calculate()
        list=[x/4 for x in arr]
        return list

    def Ranking(self):
        Ranking_list=[]
        data=self.average_Calculate()
        data_sorted=sorted(data) 
        for i in range(len(data)):
            for j in range(len(data_sorted)):
                if data[i]==data_sorted[j]:
                   Ranking_list.append(len(data)-j)
        return  Ranking_list
    def show(self):
        cell_range_pattern='c5:j12'
        cell_range = sheet[cell_range_pattern]
        for row in cell_range:
            for cell in row:
                print(cell.value, end='\t')  # Print cell value and separate with tabs
            print()  # Move to the next r

excel_file_path = r'C:\Users\Dev\Desktop\grade_list.xlsx'
# Load the Excel workbook and select the sheet
workbook = openpyxl.load_workbook(excel_file_path)
# Get the sheet names
sheet_names = workbook.sheetnames
sheet_name=sheet_names[0]
# Print the sheet names
print("Sheet names:", sheet_names)
sheet = workbook[sheet_name]
# Specify the cell coordinates (row and column indices, 1-based index)
# Access the cell range
cell_range_pattern='d6:g12'
cell_range = sheet[cell_range_pattern]

data=Excel_grade_list(cell_range)

list=data.sum_Calculate()
cell_range_pattern = 'H6:H12'
cell_range1 = sheet[cell_range_pattern]
for i, row in enumerate(cell_range1):
    cell = row[0]  
    cell.value = list[i]
    
list1=data.average_Calculate()
cell_range_pattern = 'i6:i12'
cell_range2 = sheet[cell_range_pattern]
for i, row in enumerate(cell_range2):
    cell = row[0]  
    cell.value = list1[i]
    
list2=data.Ranking()
cell_range_pattern = 'j6:j12'
cell_range3 = sheet[cell_range_pattern]
for i, row in enumerate(cell_range3):
    cell = row[0]  
    cell.value = list2[i]   
data.show()
workbook.save(r'C:\Users\Dev\Desktop\grade_list.xlsx')


data=GS_grade_list("C:/Users/Dev/Documents/github/python_course/teacher/w4/python_course_access_cred.json")
list=data.sum_Calculate()
cell_range_pattern = 'H6:H12'
cell_range1 = sheet[cell_range_pattern]
for i, row in enumerate(cell_range1):
    cell = row[0]  
    cell.value = list[i]
    
list1=data.average_Calculate()
cell_range_pattern = 'i6:i12'
cell_range2 = sheet[cell_range_pattern]
for i, row in enumerate(cell_range2):
    cell = row[0]  
    cell.value = list1[i]
    
list2=data.Ranking()
cell_range_pattern = 'j6:j12'
cell_range3 = sheet[cell_range_pattern]
for i, row in enumerate(cell_range3):
    cell = row[0]  
    cell.value = list2[i]   
data.show()








