import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_failed_students(sheet):
    all_students = sheet.get_all_records()
    failed_students = [student for student in all_students if student['Score'] < 50]
    return failed_students

def main():
    # Replace with the path to your credentials file
    credentials_file = 'C:/Users/User/Documents/GitHub/python_course/teacher/w4/python_course_access_cred.json'

    # Use the name of the sheet you want to read data from
    sheet_name = 'Sheet1'

    # Authorize access to the Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(creds)

    # Open the sheet and get the failed students
    sheet = client.open(sheet_name).sheet1
    failed_students = get_failed_students(sheet)

    # Print the failed students
    print('Failed Students:')
    for student in failed_students:
        print(f"{student['Name']} - {student['Score']}")

if __name__ == '__main__':
    main()