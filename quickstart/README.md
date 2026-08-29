# Getting Started with IronXL for Python

> Docs: [IronXL for Python documentation](https://ironsoftware.com/python/excel/docs/?utm_source=github)


IronXL for Python reads and writes Excel (XLS, XLSX, and CSV) files in Python 3 projects, with no copy of Excel installed on the server and no Interop. Its API is smaller than `Microsoft.Office.Interop.Excel`, and follows IronXL for .NET.

## Install IronXL for Python

### Prerequisites

Before installing IronXL for Python, ensure the following software is installed on your computer:

1. **.NET 6.0 SDK**: As IronXL for Python utilizes the .NET 6.0 framework from its accompanying IronXL .NET library, installing the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) is essential.
2. **Python**: Obtain the newest version of Python 3.x by visiting the [official Python website](https://www.python.org/downloads/). Ensure Python is added to your system PATH during installation to facilitate its access via the command line.
3. **Pip**: While recent Python installations come with pip, verify if pip is installed or install it if necessary.
4. **IronXL Library**: Add the IronXL library to your environment using pip with the following command:

```shell
pip install ironxl
```

To specify a version of IronXL, append `==2023.x.x` to the install command, replacing `x.x` with the desired version.

Note: On systems defaulting to Python 2.x, use `pip3` instead of `pip` to ensure the correct version of Pip is utilized.

## Reading an Excel Document

Extracting data from an Excel spreadsheet involves straightforward commands through IronXL for Python.

```python
from ironxl import WorkBook

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
```

## Creating New Excel Documents

IronXL for Python creates Excel documents from scratch.

```python
from ironxl import WorkBook, ExcelFileFormat, BorderType

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
```

## Exporting Data in Various Formats

IronXL for Python supports exporting to several popular formats.

```python
from ironxl import *

# The guide opens a workbook before this snippet; open one here so the
# example runs on its own.
workBook = WorkBook.Load("sample.xlsx")
workSheet = workBook.WorkSheets[0]

workSheet.SaveAs("NewExcelFile.xls")
workSheet.SaveAs("NewExcelFile.xlsx")
workSheet.SaveAsCsv("NewExcelFile.csv")
workSheet.SaveAsJson("NewExcelFile.json")
workSheet.SaveAsXml("NewExcelFile.xml")
```

## Cell and Range Styling

Apply styles to cells and ranges.

```python
from ironxl import *

# The guide creates a worksheet before this snippet; create one here so
# the example runs on its own.
workBook = WorkBook.Create(ExcelFileFormat.XLSX)
workSheet = workBook.CreateWorkSheet("main_sheet")

# Set cell's value and styles
workSheet["A1"].Value = "Hello World"
workSheet["A2"].Style.BottomBorder.SetColor("#ff6600")
workSheet["A2"].Style.BottomBorder.Type = BorderType.Double
```

## Sorting Cell Ranges

Sort cell values efficiently within ranges using IronXL.

```python
from ironxl import WorkBook

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
```

## Modifying Formulas

Modify and evaluate Excel formulas on-the-fly.

```python
from ironxl import *

# The guide creates a worksheet before this snippet; create one here so
# the example runs on its own.
workBook = WorkBook.Create(ExcelFileFormat.XLSX)
workSheet = workBook.CreateWorkSheet("main_sheet")

# Set a formula
workSheet["A1"].Formula = "=SUM(A2:A10)"
# Get the calculated value
sum_ = workSheet["A1"].DecimalValue
```

## Why IronXL for Python?

IronXL for Python simplifies Excel file handling with its user-friendly API, eliminating the need for Microsoft Excel or Excel Interop installations on your server.

## Licensing & Support Options

**IronXL for Python** is readily available for testing in development settings at no cost.

To deploy in production, [acquire a commercial license](https://ironsoftware.com/python/excel/licensing/?utm_source=github). [30-day trial licenses](https://ironsoftware.com/python/excel/?utm_source=github#trial-license) are available to evaluate its full capabilities.

For a comprehensive range of code samples, tutorials, license details, and documentation, visit the [IronXL for Python page](https://ironsoftware.com/python/excel/?utm_source=github).

For additional support and queries, feel free to [contact our support team](https://ironsoftware.com?utm_source=github#live-chat-support).