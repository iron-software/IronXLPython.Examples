from ironxl import WorkBook, ExcelFileFormat, BorderType  # Import necessary classes from ironxl

def run():
    # Create a new Excel WorkBook document in XLSX format
    workbook = WorkBook.create(ExcelFileFormat.XLSX)
    # Set metadata for the workbook
    workbook.metadata.author = "IronXL"
    # Add a new blank worksheet named "main_sheet" to the workbook
    worksheet = workbook.create_worksheet("main_sheet")
    # Add data to cell "A1"
    worksheet["A1"].value = "Hello World"
    # Set the style for cell "A2" with a double bottom border and a specific color
    worksheet["A2"].style.bottom_border.set_color("#ff6600")
    worksheet["A2"].style.bottom_border.type = BorderType.double
    # Save the Excel file with the specified filename
    workbook.save_as("NewExcelFile.xlsx")