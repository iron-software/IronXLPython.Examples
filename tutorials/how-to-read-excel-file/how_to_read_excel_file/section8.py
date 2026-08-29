from ironxl import *

def run():
    # The guide opens a worksheet before this snippet, and sets `i` to the
    # last row holding data. Both are established here so the example runs on
    # its own.
    workBook = WorkBook.Load("Spreadsheets\\GDP.xlsx")
    workSheet = workBook.DefaultWorkSheet
    i = workSheet.RowCount

    # Iterate through all rows with a value
    for y in range(2, i):
        # Get the C cell
        cell = workSheet[f"C{y}"]
        # Set the formula for the Percentage of Total column
        cell.Formula = f"=B{y}/B{i}"
