from ironxl import *

def run():
    # The guide creates a worksheet before this snippet; create one here so
    # the example runs on its own.
    workBook = WorkBook.Create(ExcelFileFormat.XLSX)
    workSheet = workBook.CreateWorkSheet("main_sheet")

    # Set a formula
    workSheet["A1"].Formula = "=SUM(A2:A10)"
    # Get the calculated value
    sum_ = workSheet["A1"].DecimalValue
