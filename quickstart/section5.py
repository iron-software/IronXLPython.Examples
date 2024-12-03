from ironxl import *

# Load existing spreadsheet
workbook = WorkBook.Load("sample.xls")
worksheet = workbook.WorkSheets[0]

# This is how we get a range from an Excel worksheet
selected_range = worksheet["A2:A8"]

# Sort the range in the sheet
selected_range.SortAscending()

# Save changes with the sorted range
workbook.Save()