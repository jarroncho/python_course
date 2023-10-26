

import gspread
import openpyxl
from abc import ABC,abstractmethod
class baseclass:
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def getdata(self):
        pass
    @abstractmethod
    def sum_average_rank(self):
        pass
    @abstractmethod
    def printdata(self):
        pass

class grade(baseclass):
    def __init__(self,path):
        self.path=path
    def getdata(self):

        workbook = openpyxl.load_workbook(self.path)
        sheet_names = workbook.sheetnames
        sheet_name=sheet_names[0]
        sheet = workbook[sheet_name]
        cell_range_pattern='c5:j12'
        cell_range = sheet[cell_range_pattern]
        self.grade_list=[]
        for row in cell_range:
            value=[]
            for cell in row:
                    value.append(cell.value)
            self.grade_list.append(value)
        return self.grade_list

    def sum_average_rank(self):
        self.rank=[]
        #計算平均、總和
        for i in range(1,len(self.grade_list)):
            total=sum(self.grade_list[i][1:5])
            average=total/4
            self.grade_list[i][5]=total
            self.grade_list[i][6]=average
            self.rank.append(self.grade_list[i][5])
        #排列名次
        self.rank=sorted(self.rank,reverse=True)
        #將名次放進去
        for i in range(1,len(self.grade_list)):
            self.grade_list[i][7]=self.rank.index(self.grade_list[i][5])+1

        return self.grade_list

    def printdata(self):
        for i in range(len(self.grade_list)):
            print(self.grade_list[i][0], end='\t')
            for j in range(1, len(self.grade_list[i])):
                print(self.grade_list[i][j], end='\t')
            print()  






class googledata(baseclass):

    def __init__(self):
        pass

    def getdata(self,path):
       
        gc = gspread.service_account(filename=path)
        sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1nqgiOHVyuIM1p4cBKUsi1HfmkaIhjIQdQYamGbkzOhE/edit#gid=0')

        cell_range_pattern='c5:j12'
        cell_range=sh.sheet1.get(cell_range_pattern)
        self.grade_list=[]
        for row in cell_range:
            value=[]
            for cell in row:
                    value.append(cell)
            self.grade_list.append(value)

    def sum_average_rank(self):
        self.rank=[]
        for i in range(1,len(self.grade_list)):
            total=0
            for j in range(1,5):
                total+=int(self.grade_list[i][j])
            average=total/4
            self.grade_list[i].append(total)
            self.grade_list[i].append(average)
            self.rank.append(self.grade_list[i][5])

        #排列名次
        self.rank=sorted(self.rank,reverse=True)
        #將名次放進去
        for i in range(1,len(self.grade_list)):
            self.grade_list[i].append(self.rank.index(self.grade_list[i][5])+1)

    def printdata(self):
 
        for i in range(len(self.grade_list)):
            print(self.grade_list[i][0], end='\t')
            for j in range(1, len(self.grade_list[i])):
                print(self.grade_list[i][j], end='\t')
            print()



gradelist=grade(r'C:\Users\kmsh1\Desktop\python程式設計\python_course\teacher\w3\grade_list.xlsx')        
gradelist.getdata()
gradelist.sum_average_rank()
gradelist.printdata()   


googlesheet=googledata()     
googlesheet.getdata(r'C:\Users\kmsh1\Desktop\python程式設計\python_course\teacher\w4\python_course_access_cred.json')
googlesheet.sum_average_rank()
googlesheet.printdata()   


