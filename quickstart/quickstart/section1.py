from ironxl import WorkBook

def run():
    # Load the necessary module from IronXL
    # Load an existing Excel spreadsheet
    # Replace 'sample.xlsx' with the path to your Excel file as needed.
    workbook = WorkBook.load("sample.xlsx")
    # Select the first worksheet from the workbook
    worksheet = workbook.worksheets[0]
    # Access cell A2 and get its integer value
    # Ensure the correct method or property is used to fetch the integer value.
    # Use 'value' to directly access the cell content.
    cell_value = worksheet["A2"].value
    # Print out the value of the cell A2
    # Utilizing formatted strings for clear output
    print(f"Cell A2 has value '{cell_value}'")
    # Iterate over a range of cells and print their address and text content
    # The range is defined from A2 to B10, which captures all rows in this interval.
    for cell in worksheet.range("A2:B10"):
        # Access each cell in the specified range
        # AddressString is used to get the cell's location as a string, and Text to get its content.
        print(f"Cell {cell.address} has value '{cell.text}'")