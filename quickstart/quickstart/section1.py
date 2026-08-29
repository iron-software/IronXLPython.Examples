from ironxl import WorkBook

def run():
    # Load an existing Excel spreadsheet.
    # Replace 'sample.xlsx' with the path to your Excel file as needed.
    workbook = WorkBook.Load("sample.xlsx")
    # Select the first worksheet from the workbook
    worksheet = workbook.WorkSheets[0]
    # Access cell A2 and read its value
    cell_value = worksheet["A2"].Value
    print(f"Cell A2 has value '{cell_value}'")
    # Iterate over the range A2:B10 and print each cell's address and text.
    # Indexing a worksheet with a range string returns a Range, which is
    # iterable; AddressString is the cell's location, Text its contents.
    for cell in worksheet["A2:B10"]:
        print(f"Cell {cell.AddressString} has value '{cell.Text}'")
