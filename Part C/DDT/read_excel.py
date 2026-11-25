import openpyxl

'''workbook = openpyxl.load_workbook("login_data.xlsx")
#print(workbook.sheetnames)
sheet = workbook["Login_data"]


print(sheet['A4'].value)
print(sheet['B4'].value)
print(sheet['A2'].value,sheet['B2'].value)

print(sheet.cell(row=3,column=1).value)
print(sheet.cell(row=3,column=2).value)

# for row and column
print(sheet.max_column)
print(sheet.max_row)
'''
'''for i in range(2,sheet.max_row+1):
    email = sheet.cell(row=i,column=1).value
    password = sheet.cell(row=i,column=2).value
    print(email,password)'''

'''for i in range(2,sheet.max_row+1):
    for j in range(1,sheet.max_column+1):
        print(sheet.cell(row=i,column=j).value, end=" ")
    print()
'''

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
#1) Print 1st employee details
#2) Print only names of employee
#3) Print all employee details
#4) Print total no: of rows and columns

workbook = openpyxl.load_workbook("Employee_data.xlsx")
sheet = workbook["Employee_data"]

#1) Print 1st employee details
'''print(sheet['A2'].value)
print(sheet['B2'].value)
print(sheet['C2'].value)
print(sheet['D2'].value)'''

# Print only names of employee














