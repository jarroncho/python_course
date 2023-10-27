import openpyxl

wb=openpyxl.load_workbook('C:/Users/user/Desktop/grade_list.xlsx',data_only=True)
sheet=wb['grade']
grade_list=[]

for i in sheet['c5:j12'] :
    temp=[]
    for j in i:
        temp.append(j.value)
    grade_list.append(temp)

"print(grade_list[7])"

for i in range(1,len(grade_list)):
    grade_list[i][5]=grade_list[i][1]+ grade_list[i][2]+ grade_list[i][3]+ grade_list[i][4]
    grade_list[i][6]=grade_list[i][5]/4

rank =sorted(grade_list[1:],key=lambda s: s[5],reverse=True)
"print(rank)"

for i in range(len(rank)):
    rank[i][7]=i+1

for i in range(len(grade_list)):
    print(grade_list[i][0], end='\t')
    for j in range(1, len(grade_list[i])):
        print(grade_list[i][j], end='\t')
    print()
    
    
"---------OOP----------"

class GradeList:
    
    def __init__(self, file):
        self.file= file
        
    def print_list(self):
        for i in range(len(self.grade_list)):
            print(self.grade_list[i][0], end='\t')
            for j in range(1, len(self.grade_list[i])):
                print(self.grade_list[i][j], end='\t')
            print()

    def get_list(self):
        return self.grade_list
    
    def build_list(self):
        self.wb=openpyxl.load_workbook(self.file)
        self.sheet=self.wb['grade']
        self.grade_list=[]
        for i in self.sheet['c5:j12'] :
            self.temp=[]
            for j in i:
                self.temp.append(j.value)
            self.grade_list.append(self.temp)
        
    def ranking(self):
        for i in range(1,len(self.grade_list)):
            self.grade_list[i][5]=self.grade_list[i][1]+ self.grade_list[i][2]+ self.grade_list[i][3]+ self.grade_list[i][4]
            self.grade_list[i][6]=self.grade_list[i][5]/4
        self.grade_sorted=sorted(self.grade_list[1:], key= lambda x: x[5], reverse=True)
        for i in range(len(self.grade_sorted)):
            self.grade_sorted[i][7]=i+1
 
 
print('\n' 'oop test:')
grade_list=GradeList('C:/Users/user/Desktop/grade_list.xlsx')
grade_list.build_list()
grade_list.ranking()
grade_list.print_list() 
    