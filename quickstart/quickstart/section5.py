from ironxl import WorkBook

def run():
    # Import IronXL library for handling Excel files
    # Load an existing Excel workbook
    # 'sample.xls' is the file name of the Excel workbook to be loaded
    workbook = WorkBook.Load("sample.xls")
    # Access the first worksheet in the workbook
    # WorkSheets is the collection of all sheets in the workbook, 
    # and we select the first one using index 0
    worksheet = workbook.WorkSheets[0]
    # Select a range of cells from A2 to A8 in the worksheet
    # This specifies a contiguous range of cells starting from A2 and ending at A8
    selected_range = worksheet["A2:A8"]
    # Sort the selected range of cells in ascending order
    # This operation reorders the values in the specified range from smallest to largest
    selected_range.SortAscending()
    # Save the changes made to the workbook, including the sorted range
    # The workbook's state is updated with the changes after execution
    workbook.Save()