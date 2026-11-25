import openpyxl

def get_login_data():
    workbook = openpyxl.load_workbook('C://Users//brijm//PycharmProjects//M_25_selenium_01//Part C//demoTricentis_BasePage//test_data//login_data.xlsx')
    sheet = workbook['Sheet']

    data =[]

    for row in sheet.iter_rows(min_row=2,values_only=True):
        data.append(row)

    return data


