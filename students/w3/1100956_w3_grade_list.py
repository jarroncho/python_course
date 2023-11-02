#POP
import openpyxl
file="C:/Users/a0965/.spyder-py3/grade_list.xlsx"
work=openpyxl.load_workbook(file)
sheet1=work.sheetnames
sheet2=work[sheet1[0]]
range1=sheet2['c5:j12']
grade_list=[[data.value for data in row] for row in range1]
n=[]

for i in range(1,8):
    total = sum(grade_list[i][1:5])
    average = total / 4
    grade_list[i][5] = total
    grade_list[i][6] = average
    n.append(average)

n=sorted(n,reverse=True)
for i in range(1,8):
    grade_list[i][7]=n.index(grade_list[i][6]) + 1

for i in range(len(grade_list)):
    print(grade_list[i][0], end='\t')
    for j in range(1, len(grade_list[i])):
        print(grade_list[i][j], end='\t')
    print()