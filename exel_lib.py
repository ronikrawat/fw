from xlrd import open_workbook

locator_file = r"C:\Users\ronik\Desktop\framework\framework\objects.xls"
test_data = r"C:\Users\ronik\Desktop\framework\framework\testdata.xls"


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
            row = sheet.row_values(i)  # returns list
            setattr(cls, row[0], (row[1], row[2]))
        return cls

    return add_element


def return_header(worksheet, test_case):
    book = open_workbook(test_data)
    sheet = book.sheet_by_name(worksheet)
    used_rows = sheet.nrows
    for i in range(0, used_rows):
        row = sheet.row_values(i)
        if row[0] == test_case:
            row = [line.strip()
                   for line in sheet.row_values(i-1)[2:] if line.strip()]
            return ",".join(row)


def return_test_data(worksheet, testcase):
    book = open_workbook(test_data)
    sheet = book.sheet_by_name(worksheet)
    used_rows = sheet.nrows
    data = []
    for i in range(0, used_rows):
        row = sheet.row_values(i)
        if row[0] == testcase and row[1].upper() == "YES":
            row = [line.strip() for line in row if line.strip()]
            data.append(tuple(row[2:]))
    return data
