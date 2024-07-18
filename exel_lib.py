from xlrd import open_workbook

locator_file = r"C:\Users\ronik\Desktop\framework\framework\objects.xls"


def read_locators(worksheet):
    book = open_workbook(locator_file)
    sheet = book.sheet_by_name(worksheet)
    used_rows = sheet.nrows
    data = {}
    for i in range(1, used_rows):
        row = sheet.row_values(i)
        data[row[0]] = (row[1], row[2])
    return data


def add_elements(worksheet):
    def add_element(cls):
        book = open_workbook(locator_file)
        sheet = book.sheet_by_name(worksheet)
        used_rows = sheet.nrows
        for i in range(1, used_rows):
            row = sheet.row_values(i)           # returns list
            setattr(cls, row[0], (row[1], row[2]))
        return cls
    return add_element
