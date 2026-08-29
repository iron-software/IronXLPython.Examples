from ironxl import *

def run():
    # The guide opens a worksheet before this snippet; open one here so the
    # example runs on its own.
    workBook = WorkBook.Load("Spreadsheets\\GDP.xlsx")
    workSheet = workBook.DefaultWorkSheet

    # Access range D2:D101 in the worksheet
    range_ = workSheet["D2:D101"]
