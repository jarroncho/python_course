from abc import ABC,abstractmethod
import gspread
import openpyxl
excel_file_path = 'C:\\Users\\李芷榆\\OneDrive\\桌面\\python\\grade_list.xlsx'


class base_grade_list(ABC):
    @abstractmethod
    def get_grade_list(self):
        pass
    @abstractmethod
    def calculate_sum_sort(self):
        pass
    @abstractmethod
    def printing(self):
        pass


class excel_grade_list(base_grade_list):
    def __init__(self,import_excel):
        self.import_excel=import_excel

    def get_grade_list(self):
        workbook = openpyxl.load_workbook(self.import_excel)
        sheet_names = workbook.sheetnames
        sheet_name=sheet_names[0]
        sheet = workbook[sheet_name]
        cell_range_pattern='c5:j12'
        cell_range = sheet[cell_range_pattern]

        self.grade_table=[]
        for i in cell_range:
            line=[]
            for j in i:
                line.append(j.value)
            self.grade_table.append(line)
        workbook.close
        self.a=[]

    def calculate_sum_sort(self):
   
        for i in range(1,len(self.grade_table)):
            self.grade_table[i][5]=0
            self.grade_table[i][6]=0
            self.grade_table[i][7]=0
            
        for i in range(1,len(self.grade_table)):
            sum=0
            for j in range(1,len(self.grade_table[i])-3):
                sum+=self.grade_table[i][j]
            self.grade_table[i][5]=sum
            self.grade_table[i][6]=sum/4
            self.a.append(self.grade_table[i][5])

        self.a.sort(reverse=True)
        for i in range(1,len(self.grade_table)):
            self.grade_table[i][7]=self.a.index(self.grade_table[i][5])+1

    def printing(self):
        for i in range(len(self.grade_table)):
            print(self.grade_table[i][0], end='\t')
            for j in range(1, len(self.grade_table[i])):
                print(self.grade_table[i][j], end='\t')
            print('\n')
        print('\n')

class GS_grade_list(base_grade_list):
    def __init__(self,sh):
        self.sh=sh

    def get_grade_list(self):
        gc = gspread.service_account(filename=self.sh)
        sh =gc.open_by_url('https://docs.google.com/spreadsheets/d/1nqgiOHVyuIM1p4cBKUsi1HfmkaIhjIQdQYamGbkzOhE/edit#gid=0')
        cell_range_pattern='c5:j12'
        cell_range=sh.sheet1.get(cell_range_pattern)
        self.grade_list_data=list(cell_range)
        self.a=[]
    def calculate_sum_sort(self):
        
        for i in range(1,len(self.grade_list_data)):
            self.grade_list_data[i][5]=0
            self.grade_list_data[i][6]=0
            self.grade_list_data[i][7]=0
        for i in range(1,len(self.grade_list_data)):
            sum=0
            for j in range(1,len(self.grade_list_data[i])-3):
                sum+=int(self.grade_list_data[i][j])
            self.grade_list_data[i][5]=sum
            self.grade_list_data[i][6]=sum/4
            self.a.append(self.grade_list_data[i][5])

        self.a.sort(reverse=True)
        for i in range(1,len(self.grade_list_data)):
            self.grade_list_data[i][7]=self.a.index(self.grade_list_data[i][5])+1
        
    def printing(self):
        for i in range(len(self.grade_list_data)):
            print(self.grade_list_data[i][0], end='\t')
            for j in range(1, len(self.grade_list_data[i])):
                print(self.grade_list_data[i][j], end='\t')
            print('\n')
        print('\n')

#testexcel
excel_test=excel_grade_list(excel_file_path)
excel_test.get_grade_list()
excel_test.calculate_sum_sort()
excel_test.printing

#testgs
gs_test=GS_grade_list('D:\\github\\python_course\\teacher\\w4\\python_course_access_cred.json')
gs_test.get_grade_list()
gs_test.calculate_sum_sort()
gs_test.printing()
