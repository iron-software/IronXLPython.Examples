from ironxl import *

def run():
    # The guide opens a workbook before this snippet; open one here so the
    # example runs on its own.
    workBook = WorkBook.Load("sample.xlsx")
    workSheet = workBook.WorkSheets[0]

    workSheet.SaveAs("NewExcelFile.xls")
    workSheet.SaveAs("NewExcelFile.xlsx")
    workSheet.SaveAsCsv("NewExcelFile.csv")
    workSheet.SaveAsJson("NewExcelFile.json")
    workSheet.SaveAsXml("NewExcelFile.xml")
