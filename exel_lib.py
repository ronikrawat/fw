from xlrd import open_workbook


def read_locators(worksheet):
    book = open_workbook(r"C:\Users\ronik\Desktop\framework\framework\objects.xls")
    sheet = book.sheet_by_name(worksheet)
    used_rows = sheet.nrows
    data = {}
    for i in range(1, used_rows):
        row = sheet.row_values(i)
        data[row[0]] = (row[1], row[2])
    return data

