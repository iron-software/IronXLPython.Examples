from ironxl import *

def run():
    # The guide creates a worksheet before this snippet; create one here so
    # the example runs on its own.
    workBook = WorkBook.Create(ExcelFileFormat.XLSX)
    workSheet = workBook.CreateWorkSheet("main_sheet")

    # Set cell's value and styles
    workSheet["A1"].Value = "Hello World"
    workSheet["A2"].Style.BottomBorder.SetColor("#ff6600")
    workSheet["A2"].Style.BottomBorder.Type = BorderType.Double
