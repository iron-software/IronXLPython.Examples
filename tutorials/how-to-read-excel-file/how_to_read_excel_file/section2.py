from ironxl import *

def run():
    # The guide loads a workbook before this snippet; load one here so the
    # example runs on its own.
    workBook = WorkBook.Load("Spreadsheets\\GDP.xlsx")

    workSheet = workBook.GetWorkSheet("GDPByCountry")
