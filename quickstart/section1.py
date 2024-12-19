from ironxl import *

def run():
    # Load existing spreadsheet
    workbook = WorkBook.Load("sample.xlsx")
    worksheet = workbook.WorkSheets[0]
    # Select cells easily in Excel notation and return the calculated value, date, text, or formula
    cell_value = worksheet["A2"].IntValue
    # Read from ranges of cells elegantly
    for cell in worksheet["A2:B10"]:
        print(f"Cell {cell.AddressString} has value '{cell.Text}'")