# Introduction to IronXL for Python

***Based on <https://ironsoftware.com/docs/docs/>***


IronXL for Python is an advanced library developed by Iron Software. It allows developers to effortlessly create, read, and manage Excel files such as XLS, XLSX, and CSV within Python 3 environments.

This library operates independently of Excel, eliminating the need for Excel or Interop on your server. It offers a more accessible and swifter API compared to **Microsoft.Office.Interop.Excel** and extends the functionalities initially available in IronXL for .NET.

## Installing IronXL for Python

### System Requirements

Before installing IronXL for Python, make sure your system meets these requirements:

1. **.NET 6.0 SDK**: As IronXL for Python utilizes the .NET 6.0 framework through the IronXL .NET library, the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) is necessary.
2. **Python**: Install the most recent Python 3.x release from [Python’s official site](https://www.python.org/downloads/). Include Python in the system PATH to execute it from any command line interface.
3. **Pip**: Starting from Python 3.4, Pip is included by default. Confirm its presence or install it if absent.
4. **IronXL Library**: Add IronXL to your project via pip with the command:

```shell
pip install ironxl
```

For specific releases, use the syntax "==YYYY.M.D", such as "pip install IronXL==2023.1.1". If Python 2.x conflicts, you might need the `pip3` command.

## Reading an Excel Document

Extract data from Excel with minimal code:

```python
from ironxl import *

# Open an existing Excel file

***Based on <https://ironsoftware.com/docs/docs/>***

workbook = WorkBook.Load("sample.xlsx")
worksheet = workbook.WorkSheets[0]

# Directly access cells with Excel notation

***Based on <https://ironsoftware.com/docs/docs/>***

cell_value = worksheet["A2"].IntValue

# Process multiple cells with ease

***Based on <https://ironsoftware.com/docs/docs/>***

for cell in worksheet["A2:B10"]:
    print(f"Cell {cell.AddressString} contains '{cell.Text}'")
```

## Creating New Excel Documents

IronXL simplifies the creation of Excel files in Python:

```python
from ironxl import *

# Initialize a new Excel workbook

***Based on <https://ironsoftware.com/docs/docs/>***

workbook = WorkBook.Create(ExcelFileFormat.XLSX)
workbook.Metadata.Author = "Iron Software"

# Add and populate a worksheet

***Based on <https://ironsoftware.com/docs/docs/>***

worksheet = workbook.CreateWorkSheet("new_sheet")
worksheet["A1"].Value = "Hello World"
worksheet["A2"].Style.BottomBorder.SetColor("#ff6600")
worksheet["A2"].Style.BottomBorder.Type = BorderType.Double

# Save the document

***Based on <https://ironsoftware.com/docs/docs/>***

workbook.SaveAs("NewExcelDocument.xlsx")
```

## Exporting Document Formats

IronXL supports converting to various file formats:

```python
# Assume workSheet is already created

***Based on <https://ironsoftware.com/docs/docs/>***

workSheet.SaveAs("ExcelDocument.xls")
workSheet.SaveAs("ExcelDocument.xlsx")
workSheet.SaveAsCsv("ExcelDocument.csv")
workSheet.SaveAsJson("ExcelDocument.json")
workSheet.SaveAsXml("ExcelDocument.xml")
```

## Styling Cells and Ranges with IronXL

Apply styles to cells and ranges efficiently:

```python
# Define cell properties and styles

***Based on <https://ironsoftware.com/docs/docs/>***

workSheet["A1"].Value = "Hello World"
workSheet["A2"].Style.BottomBorder.SetColor("#ff6600")
workSheet["A2"].Style.BottomBorder.Type = BorderType.Double
```

## Sorting Ranges in Excel

Effortlessly sort data in Excel files using IronXL:

```python
from ironxl import *

# Load an existing spreadsheet

***Based on <https://ironsoftware.com/docs/docs/>***

workbook = WorkBook.Load("sample.xls")
worksheet = workbook.WorkSheets[0]

# Select a data range

***Based on <https://ironsoftware.com/docs/docs/>***

selected_range = worksheet["A2:A8"]

# Apply ascending sort

***Based on <https://ironsoftware.com/docs/docs/>***

selected_range.SortAscending()

# Save the sorted workbook

***Based on <https://ironsoftware.com/docs/docs/>***

workbook.Save()
```

## Editing Formulas Simplified

Handling formulas is straightforward with IronXL:

```python
# Define a formula

***Based on <https://ironsoftware.com/docs/docs/>***

workSheet["A1"].Formula = "=SUM(A2:A10)"
# Retrieve the calculation

***Based on <https://ironsoftware.com/docs/docs/>***

sum_value = workSheet["A1"].DecimalValue
```

## Choosing IronXL for Python

IronXL offers a user-friendly API for Python developers to handle Excel files without installing Excel or requiring Excel Interop, simplifying document management in Python applications.

## Licensing and Support

**IronXL for Python** is free for testing in development environments.

For production, [obtain a license here](https://ironsoftware.com/python/excel/licensing/). A 30-day trial license is also available [here](https://ironsoftware.com/trial-license).

All detailed code samples, tutorials, and further licensing details can be found at [IronXL for Python](https://ironsoftware.com/python/excel/).

For additional help, don't hesitate to [contact our team](https://ironsoftware.com/#live-chat-support).