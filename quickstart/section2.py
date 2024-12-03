from ironxl import *

# Create a new Excel WorkBook document.
workbook = WorkBook.Create(ExcelFileFormat.XLSX)
workbook.Metadata.Author = "IronXL"

# Add a blank WorkSheet
worksheet = workbook.CreateWorkSheet("main_sheet")

# Add data and styles to the new worksheet
worksheet["A1"].Value = "Hello World"
worksheet["A2"].Style.BottomBorder.SetColor("#ff6600")
worksheet["A2"].Style.BottomBorder.Type = BorderType.Double  # Assuming BorderType is accessible directly

# Save the Excel file
workbook.SaveAs("NewExcelFile.xlsx")