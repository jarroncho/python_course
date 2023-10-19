


import openpyxl

#pop
print("pop")

#get data
excel_file_path = r'C:\Users\kmsh1\Desktop\python程式設計\python_course\teacher\w3\grade_list.xlsx'

workbook = openpyxl.load_workbook(excel_file_path)
sheet_names = workbook.sheetnames
sheet_name=sheet_names[0]
sheet = workbook[sheet_name]
cell_range_pattern='c5:j12'
cell_range = sheet[cell_range_pattern]
grade_list=[]
for row in cell_range:
   value=[]
   for cell in row:
        value.append(cell.value)
   grade_list.append(value)

rank=[]
#計算平均、總和
for i in range(1,len(grade_list)):
    total=sum(grade_list[i][1:5])
    average=total/4
    grade_list[i][5]=total
    grade_list[i][6]=average
    rank.append(grade_list[i][5])
#排列名次
rank=sorted(rank,reverse=True)
#將名次放進去
for i in range(1,len(grade_list)):
    grade_list[i][7]=rank.index(grade_list[i][5])+1

print('姓名\t國文\t英文\t數學\t理化\t總分\t平均\t名次')
print('------------------------------------------------------------')
for i in range(len(grade_list)):
    print(grade_list[i][0], end='\t')
    for j in range(1, len(grade_list[i])):
        print(grade_list[i][j], end='\t')
    print()

print("\n\n")
print("oop")

class grade:
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
            self.grade_list[i][7]=rank.index(self.grade_list[i][5])+1
    
        return self.grade_list
    
    def printdata(self):
        print('姓名\t國文\t英文\t數學\t理化\t總分\t平均\t名次')
        print('------------------------------------------------------------')
        for i in range(len(self.grade_list)):
            print(self.grade_list[i][0], end='\t')
            for j in range(1, len(self.grade_list[i])):
                print(self.grade_list[i][j], end='\t')
            print()  
    


gradelist=grade(r'C:\Users\kmsh1\Desktop\python程式設計\python_course\teacher\w3\grade_list.xlsx')        
gradelist.getdata()
gradelist.sum_average_rank()
gradelist.printdata()

