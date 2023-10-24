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
    def __init__(self, gs_cred_path):
        self.gs_cred_path = gs_cred_path

    def accessToData(self, dataRange):
        gc = gspread.service_account(filename=self.gs_cred_path)
        sh = gc.open_by_url(
            "https://docs.google.com/spreadsheets/d/1nqgiOHVyuIM1p4cBKUsi1HfmkaIhjIQdQYamGbkzOhE/edit#gid=0")
        cell_range = sh.sheet1.get(dataRange)
        return cell_range

    def calSumAndAvg(self, grade_list):
        rankList = []
        for i in range(1, 8):
            grade_list[i].append(0)
            for j in range(1, 5):
                grade_list[i][5] += int(grade_list[i][j])
            rankList.append(grade_list[i][5])
            grade_list[i].append(0)
            grade_list[i][6] = grade_list[i][5] / 4
        return grade_list, rankList

    def calSort(self, grade_list, rankList):
        rankList.sort()
        for i in range(1, 8):
            grade_list[i].append(0)
            grade_list[i][7] = rankList.index(grade_list[i][5]) + 1
        return grade_list

    def printing(self, grade_list):
        print("GS_grade_list")
        for i in range(8):
            for j in range(8):
                print(grade_list[i][j], end='\t')
            if i == 0:
                print(
                    '\n------------------------------------------------------------', end="")
            print()


grade = Excel_grade_list(
    "C:/Users/user/Desktop/shell/pythonCourse/dataset/grade_list.xlsx")
grade_list = grade.accessToData('c5:j12')
grade_list, rankList = grade.calSumAndAvg(grade_list)
grade_list = grade.calSort(grade_list, rankList)
grade.printing(grade_list)

gs = GS_grade_list(
    "pythonCourse\dataset\python_course_access_cred.json")
gs_list = gs.accessToData('c5:j12')
gs_list, rank = gs.calSumAndAvg(gs_list)
gs_list = gs.calSort(gs_list, rank)
gs.printing(gs_list)
