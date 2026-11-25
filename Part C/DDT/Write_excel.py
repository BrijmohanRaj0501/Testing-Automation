import openpyxl

'''workbook =openpyxl.Workbook()
sheet = workbook.active
sheet.title="Login_data"

sheet['A1'] = "Email_id"
sheet['B1'] = "Password"

sheet['A2'] = "Tom@gmail.com"
sheet['B2'] = "tom@1234"

sheet['A3'] = "jerry@gmail.com"
sheet['B3'] = "Jerry@1234"

sheet['A4'] = "Motu@gmail.com"
sheet['B4'] = "Mouse@1234"

sheet.cell(row=5,column=1).value="patlu@gmail.com"
sheet.cell(row=5,column=2).value="patlu@1234"

sheet.cell(row=6,column=1).value ="bheem@gmail.com"
sheet.cell(row=6,column=2).value="patlu@1234"

workbook.save("Login_data.xlsx")'''

#task--01
'''
Create an excel named Employee_Data.xlsx with sheetname  as Employee_Details

Emp_ID     Name         Department        Salary

E101      Ram           Development       30000
E102      Joy           Testing           35000
E103      Beena         HR                30000
E104      Teena         DevOps            40000
E105      Daniel        Operations        25000
'''
workbook =openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Employee_data"

sheet['A1'] = "Emp_id"
sheet['B1'] = "Name"
sheet['C1'] = "Department"
sheet['D1'] = "Salary"


sheet['A2'] = "E101"
sheet['B2'] = "Ram"
sheet['C2'] = "Development"
sheet['D2'] = "30000"

sheet['A3'] = "E102"
sheet['B3'] = "Joy"
sheet['C3'] = "Testing"
sheet['D3'] = "35000"

sheet['A4'] = "E103"
sheet['B4'] = "Beena"
sheet['C4'] = "HR"
sheet['D4'] = "30000"

sheet['A5'] = "E104"
sheet['B5'] = "Teena"
sheet['C5'] = "DevOps"
sheet['D5'] = "40000"

sheet['A6'] = "E105"
sheet['B6'] = "Daniel"
sheet['C6'] = "Operational"
sheet['D6'] = "25000"

workbook.save("Employee_data.xlsx")








