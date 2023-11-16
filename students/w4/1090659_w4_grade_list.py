from abc import ABC, abstractmethod

import gspread
import openpyxl

class Base_Grade_list(ABC):
    @abstractmethod
    def accessToData(self):
        pass

    @abstractmethod
    def calSumAndAvg(self):
        pass

    @abstractmethod
    def calSort(self):
        pass

    @abstractmethod
    def printing(self):
        pass

class Excel_grade_list(Base_Grade_list):
    def __init__(self, excel_file_path):
        self.excel_file_path = excel_file_path

    def accessToData(self, dataRange):
        workbook = openpyxl.load_workbook(self.excel_file_path)
        sheet_names = workbook.sheetnames
        sheet = workbook[sheet_names[0]]
        cell_range = sheet[dataRange]
        grade_list = [[data.value for data in row] for row in cell_range]
        workbook.close()
        return grade_list

    def calSumAndAvg(self, grade_list):
        rankList = []
        for i in range(1, 8):
            grade_list[i][5] = 0
            for j in range(1, 5):
                grade_list[i][5] += grade_list[i][j]
            rankList.append(grade_list[i][5])
            grade_list[i][6] = 0
            grade_list[i][6] = grade_list[i][5] / 4
        return grade_list, rankList

    def calSort(self, grade_list, rankList):
        rankList.sort()
        for i in range(1, 8):
            grade_list[i][7] = rankList.index(grade_list[i][5]) + 1
        return grade_list

    def printing(self, grade_list):
        print("Excel_grade_list")
        for i in range(8):
            for j in range(8):
                print(grade_list[i][j], end='\t')
            if i == 0:
                print(
                    '\n------------------------------------------------------------', end="")
            print()



class GS_grade_list(Base_Grade_list):
    def __init__(self, file_data):
        self.file_data = file_data

    def accessToData(self, dataRange):
        gc = gspread.service_account(self.file_data)
        sh = gc.open_by_url(
            "https://docs.google.com/spreadsheets/d/1nqgiOHVyuIM1p4cBKUsi1HfmkaIhjIQdQYamGbkzOhE/edit#gid=0")
        cell_range = sh.sheet1.get(dataRange)
        return cell_range

    def grade_list(self):
        # total score
        length = len(self.grade_list_data[0])
        print("length=",length)
        print("self.grade_list_data[0]=",self.grade_list_data[0])
        print('self.grade_list_data[1][1]=',self.grade_list_data[1][1])     #john的國文
        print('self.grade_list_data[1][5]=', self.grade_list_data[1][5])  # john的total
        for i in range(1, length):
            score = 0
            for j in range(1, 4):
                self.grade_list_data[i][j] = int(self.grade_list_data[i][j])
                score += self.grade_list_data[i][j]
                # print("score=",score)
            self.grade_list_data[i][5]=score
            average = float(self.grade_list_data[i][5]) / 4
            self.grade_list_data[i][6]=average
        # rank
        data = [(1, self.grade_list_data[1][5]), (2, self.grade_list_data[2][5]), (3, self.grade_list_data[3][5]),
                (4, self.grade_list_data[4][5]), (5, self.grade_list_data[5][5]), (6, self.grade_list_data[6][5]),
                (7, self.grade_list_data[7][5])]
        sorted_data = sorted(data, key=lambda x: x[1])
        x = sorted_data[0][0]
        print("data=",data)
        print("sorted_data=",sorted_data)

        # cell_values_2d[x-1][7]=7
        for i in range(0, 7):
            x = sorted_data[i][0]
            #print(x)
            print(self.grade_list_data[x][0],self.grade_list_data[x][5])
            self.grade_list_data[x][7] = 7 - i

    def print(self):
        length = len(self.grade_list_data[0])
        for i in range(length):
            print('\t',self.grade_list_data[i][0], end='\t')
            for j in range(1, length ):
                print(self.grade_list_data[i][j], end='\t\t')
            print()

googlesheet_test = gs_data(r'D:\Python Scripts\python_course\teacher\w4\python_course_access_cred.json')
googlesheet_test.get_data()
googlesheet_test.grade_list()
googlesheet_test.print()