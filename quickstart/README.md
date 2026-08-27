# Getting Started with IronXL for Python

> Docs: [IronXL for Python documentation](https://ironsoftware.com/python/excel/docs/)


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
# Import WorkBook from IronXL

from ironxl import WorkBook

# Open an existing Excel file

workbook = WorkBook.load("sample.xlsx")

# Get the first worksheet in the workbook

worksheet = workbook.worksheets[0]

# Fetch the value from cell A2 as an integer

cell_value = worksheet["A2"].value

# Display the value of cell A2

print(f"The value in cell A2 is {cell_value}")

# Loop through cells from A2 to B10 and print their contents

for cell in worksheet.range("A2:B10"):
    print(f"Cell {cell.address} contains {cell.text}")
```

## Creating New Excel Documents

IronXL for Python creates Excel documents from scratch.

```python
from ironxl import WorkBook, ExcelFileFormat, BorderType  # Essential imports from ironxl

# Instantiate a new Excel workbook in XLSX format

workbook = WorkBook.create(ExcelFileFormat.XLSX)

# Set workbook metadata

workbook.metadata.author = "IronXL"

# Add and name a new worksheet

worksheet = workbook.create_worksheet("main_sheet")

# Populate data in cell "A1"

worksheet["A1"].value = "Hello World"

# Style cell "A2" with a specific border and color

worksheet["A2"].style.bottom_border.set_color("#ff6600")
worksheet["A2"].style.bottom_border.type = BorderType.double

# Save the workbook to a file

workbook.save_as("NewExcelFile.xlsx")
```

## Exporting Data in Various Formats

IronXL for Python supports exporting to several popular formats.

```python
# Assuming workSheet is initialized

workSheet.save_as("NewExcelFile.xls")
workSheet.save_as("NewExcelFile.xlsx")
workSheet.save_as_csv("NewExcelFile.csv")
workSheet.save_as_json("NewExcelFile.json")
workSheet.save_as_xml("NewExcelFile.xml")
```

## Cell and Range Styling

Apply styles to cells and ranges.

```python
# Define cell content and style settings

workSheet["A1"].value = "Hello World"
workSheet["A2"].style.bottom_border.set_color("#ff6600")
workSheet["A2"].style.bottom_border.type = BorderType.double
```

## Sorting Cell Ranges

Sort cell values efficiently within ranges using IronXL.

```python
# Import required components

from ironxl import WorkBook

# Load the workbook

workbook = WorkBook.load("sample.xls")

# Select the first worksheet

worksheet = workbook.worksheets[0]

# Define a cell range

selected_range = worksheet.range("A2:A8")

# Sort the range in ascending order

selected_range.sort_ascending()

# Save the updated workbook

workbook.save()
```

## Modifying Formulas

Modify and evaluate Excel formulas on-the-fly.

```python
# Directly assign a formula to a cell

workSheet["A1"].formula = "=SUM(A2:A10)"
# Retrieve and display the calculated value

sum_value = workSheet["A1"].decimal_value
```

## Why IronXL for Python?

IronXL for Python simplifies Excel file handling with its user-friendly API, eliminating the need for Microsoft Excel or Excel Interop installations on your server.

## Licensing & Support Options

**IronXL for Python** is readily available for testing in development settings at no cost.

To deploy in production, [acquire a commercial license](https://ironsoftware.com/python/excel/licensing/). [30-day trial licenses](https://ironsoftware.com/python/excel/trial-license) are available to evaluate its full capabilities.

For a comprehensive range of code samples, tutorials, license details, and documentation, visit the [IronXL for Python page](https://ironsoftware.com/python/excel/).

For additional support and queries, feel free to [contact our support team](https://ironsoftware.com#live-chat-support).