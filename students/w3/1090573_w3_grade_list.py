#1090573
import openpyxl
import pandas as pd

# Define the Excel file path (Modify this path according to your system)
excel_file_path = r'C:/Users/User\Desktop/python_course/teacher/w3/grade_list.xlsx'

# Load the Excel workbook and select the sheet
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active

# Get the data from the sheet
grade_data = [[cell.value for cell in row] for row in sheet.iter_rows(min_row=5, max_row=12, min_col=3, max_col=10)]
headers = grade_data[0]
grade_data = grade_data[1:]

# Convert the data to a DataFrame for easier processing
grade_df = pd.DataFrame(grade_data, columns=headers)

# POP Method
def calculate_metrics_pop(df):
    df['總分'] = df[['國文', '英文', '數學', '理化']].sum(axis=1)
    df['平均'] = df['總分'] / 4
    df['名次'] = df['總分'].rank(method='min', ascending=False).astype(int)
    return df

grade_df_pop = calculate_metrics_pop(grade_df)

# OOP Method
class GradeCalculatorOOP:
    def __init__(self, df):
        self.df = df
        
    def calculate_metrics(self):
        self.df['總分'] = self.df[['國文', '英文', '數學', '理化']].sum(axis=1)
        self.df['平均'] = self.df['總分'] / 4
        self.df['名次'] = self.df['總分'].rank(method='min', ascending=False).astype(int)
        return self.df

grade_calculator_oop = GradeCalculatorOOP(grade_df)
grade_df_oop = grade_calculator_oop.calculate_metrics()

# Print the results
print("總分\t平均\t名次")
print("-" * 30)
for index, row in grade_df_oop.iterrows():
    print(f"{row['總分']}\t{row['平均']:.2f}\t{row['名次']}")
