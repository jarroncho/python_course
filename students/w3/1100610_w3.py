import openpyxl
excel_file_path = 'grade_list.xlsx'
workbook = openpyxl.load_workbook(excel_file_path)
sheet_names = workbook.sheetnames

sheet_name=sheet_names[0]
sheet = workbook[sheet_name]

cell_range_pattern='c5:j12'
cell_range = sheet[cell_range_pattern]

cell_values_2d = []

for row in sheet[cell_range_pattern]:
    row_values = []  
    for cell in row:
        row_values.append(cell.value)
    cell_values_2d.append(row_values)  

for row_values in cell_values_2d[0]:
    print(row_values,end='\t')
print('\n')
del cell_values_2d [ 0 ]

grade_list=cell_values_2d   
    
class grade:
    def __init__(self, name,chinese,eng,math,sci):
        self.name = name
        self.chinese = chinese
        self.eng = eng
        self.math = math
        self.sci = sci
        self.sum1 = (chinese+eng+math+sci)
        self.avg = self.sum1/4
        self.rank = 0    
g=[]
for i in range(len(grade_list)):
    g.append(grade(grade_list[i][0],grade_list[i][1],grade_list[i][2],grade_list[i][3],grade_list[i][4]))
rank=[]
for i in range(len(grade_list)):
    rank.append(g[i].avg)
x2.sort(reverse=True)
for  i in range(len(grade_list)):
    g[i].rank=x2.index(g[i].avg)+1
for i in range(len(grade_list)):
    print(g[i].name,end='\t')
    print(g[i].chinese,end='\t')
    print(g[i].eng,end='\t')
    print(g[i].math,end='\t')
    print(g[i].sci,end='\t')
    print(g[i].sum1,end='\t')
    print(g[i].avg,end='\t')
    print(g[i].rank)
    