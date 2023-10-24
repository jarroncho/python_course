#pip install gspread oauth2client
from pathlib import Path
import gspread
from abc import ABC, abstractmethod


class List1(ABC):

    @abstractmethod
    def resizee(self):
        pass

    @abstractmethod
    def sumAvg(self):
        pass

    @abstractmethod
    def rank(self):
        pass

    @abstractmethod
    def printt(self):
        pass



class gradeList(List1):
    def __init__(self):
        self.gc = gspread.service_account(filename=Path('C:\python 程式設計\.json'))
        self.sh = self.gc.open_by_url('https://docs.google.com/spreadsheets/d/1nqgiOHVyuIM1p4cBKUsi1HfmkaIhjIQdQYamGbkzOhE/edit#gid=0')
        self.cell_range_pattern='c5:j12'
        self.cell_range=self.sh.sheet1.get(self.cell_range_pattern)
        self.grade_list_data=list(self.cell_range)
        self.cell_values_2d=[]

        print(self.cell_range)
        print(self.grade_list_data)

        self.resizee()
        self.sumAvg()
        self.rank()
        self.printt()
        


    def resizee(self):
        
        for i in range(1,len(self.grade_list_data)):
            j=0
            while j<3:
                self.grade_list_data[i].append(0)
                j+=1

    def sumAvg(self):
        for i in range(1,len(self.grade_list_data)):
            sum=0
            for j in range(1,5):
                sum+=int(self.grade_list_data[i][j])
                self.grade_list_data[i][5]=sum
                self.grade_list_data[i][6]=sum/4

    def rank(self):
        A=[]
        for i in range(1,len(self.grade_list_data)):
            A.append(int(self.grade_list_data[i][5]))
        A.sort()
        A.reverse()

        for i in range(1,len(self.grade_list_data)):
            self.grade_list_data[i][7]=A.index(self.grade_list_data[i][5])+1

    def printt(self):
         for i in range(len(self.grade_list_data)):
            for j in range(8):
                 print(self.grade_list_data[i][j],end='\t')
            print()

A=gradeList()


