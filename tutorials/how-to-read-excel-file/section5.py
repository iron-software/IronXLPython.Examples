# Load existing spreadsheet
workbook = WorkBook.Load("test.xlsx")
worksheet = workbook.DefaultWorkSheet

# Access cell B1 in the worksheet
cell = worksheet["B1"]