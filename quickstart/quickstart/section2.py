from ironxl import WorkBook, ExcelFileFormat, BorderType

def run():
    # Create a new Excel WorkBook document in XLSX format
    workbook = WorkBook.Create(ExcelFileFormat.XLSX)
    # Set metadata for the workbook
    workbook.Metadata.Author = "IronXL"
    # Add a new blank worksheet named "main_sheet" to the workbook
    worksheet = workbook.CreateWorkSheet("main_sheet")
    # Add data to cell "A1"
    worksheet["A1"].Value = "Hello World"
    # Set the style for cell "A2" with a double bottom border and a specific color
    worksheet["A2"].Style.BottomBorder.SetColor("#ff6600")
    worksheet["A2"].Style.BottomBorder.Type = BorderType.Double
    # Save the Excel file with the specified filename
    workbook.SaveAs("NewExcelFile.xlsx")
