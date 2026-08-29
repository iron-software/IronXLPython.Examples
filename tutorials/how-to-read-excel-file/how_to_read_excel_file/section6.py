from ironxl import *

def run():
    # The guide opens a worksheet before this snippet; open one here so the
    # example runs on its own.
    workBook = WorkBook.Load("Spreadsheets\\GDP.xlsx")
    workSheet = workBook.DefaultWorkSheet

    # Access cell B1 in the worksheet
    cell = workSheet["B1"]
    # Read the value of the cell as a string
    value = cell.StringValue
    print(value)
    # Write a new value to the cell
    cell.Value = "10.3289"
    print(cell.StringValue)
