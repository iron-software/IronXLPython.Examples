from ironxl import *

def run():
    # The guide creates a workbook before this snippet; create one here so the
    # example runs on its own.
    workBook = WorkBook.Create(ExcelFileFormat.XLSX)

    workSheet = workBook.CreateWorkSheet("GDPByCountry")
