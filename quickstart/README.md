# Exploring IronXL for Python

***Based on <https://ironsoftware.com/docs/docs/>***


IronXL for Python is an advanced library by Iron Software, aimed at empowering developers to manage and manipulate Excel files (including XLS, XLSX, and CSV formats) directly from Python 3 environments.

IronXL for Python operates independently of Microsoft Excel, which means there's no need for Excel installation or Interop services. It brings to the table an API that is both swifter and more streamlined than **Microsoft.Office.Interop.Excel**.

The library extends the established IronXL for .NET, leveraging its widespread acceptance and success.

## Setting Up IronXL for Python

### System Requirements

To get started with IronXL for Python, ensure your system meets the following requirements:

1. **.NET 6.0 SDK**: Given that IronXL for Python is based on the IronXL .NET library, it's critical to have the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) installed.

2. **Python**: Install the newest iteration of Python 3.x from [the official Python repository](https://www.python.org/downloads/). During setup, opt to include Python in your system PATH to ensure it is callable from any command line interface.

3. **Pip**: Most Python setups post-3.4 include Pip. Verify its presence or install it if absent.
4. **IronXL Library**: Add the IronXL library using pip with the simple command:

   ```shell
   pip install ironxl
   ```

   To target a specific release of IronXL, adjust the installation command as follows: "pip install IronXL==2023.x.x".
   On certain setups where Python 2.x is default, using `pip3` might be necessary to ensure Python 3 compatibility.

## How to Read Excel Data

Extracting data from Excel is straightforward with a few lines of Python code:

```python
from ironxl import *

# Open an existing Excel file

***Based on <https://ironsoftware.com/docs/docs/>***

workbook = WorkBook.Load("sample.xlsx")
worksheet = workbook.WorkSheets[0]

# Accessing cells directly with Excel-like references and extracting various types of values

***Based on <https://ironsoftware.com/docs/docs/>***

cell_value = worksheet["A2"].IntValue

# Loop through a range of cells to read their contents

***Based on <https://ironsoftware.com/docs/docs/>***

for cell in worksheet["A2:B10"]:
    print(f"Cell {cell.AddressString} has value '{cell.Text}'")
```

## Generating New Excel Documents

IronXL for Python simplifies the process of creating Excel documents:

```python
from ironxl import *

# Initialize a new Excel Workbook

***Based on <https://ironsoftware.com/docs/docs/>***

workbook = WorkBook.Create(ExcelFileFormat.XLSX)
workbook.Metadata.Author = "IronXL"

# Insert a fresh Worksheet

***Based on <https://ironsoftware.com/docs/docs/>***

worksheet = workbook.CreateWorkSheet("main_sheet")

# Populate cells and apply styles

***Based on <https://ironsoftware.com/docs/docs/>***

worksheet["A1"].Value = "Hello World"
worksheet["A2"].Style.BottomBorder.SetColor("#ff6600")
worksheet["A2"].Style.BottomBorder.Type = BorderType.Double

# Store the document

***Based on <https://ironsoftware.com/docs/docs/>***

workbook.SaveAs("NewExcelFile.xlsx")
```

## Exporting Formats

Saving or exporting data in various structured spreadsheet formats is effortless:

```python
# Assuming workSheet represents a current WorkSheet object

***Based on <https://ironsoftware.com/docs/docs/>***

workSheet.SaveAs("NewExcelFile.xls")
workSheet.SaveAs("NewExcelFile.xlsx")
workSheet.SaveAsCsv("NewExcelFile.csv")
workSheet.SaveAsJson("NewExcelFile.json")
workSheet.SaveAsXml("NewExcelFile.xml")
```

## Adjusting Cell and Range Styles

Applying styles to cells and ranges is achieved through the Style object:

```python
# Define cell values and styles

***Based on <https://ironsoftware.com/docs/docs/>***

workSheet["A1"].Value = "Hello World"
workSheet["A2"].Style.BottomBorder.SetColor("#ff6600")
workSheet["A2"].Style.BottomBorder.Type = BorderType.Double
```

## Sorting Cell Ranges

IronXL for Python allows for easy sorting of Excel cell ranges:

```python
from ironxl import *

# Access an existing spreadsheet

***Based on <https://ironsoftware.com/docs/docs/>***

workbook = WorkBook.Load("sample.xls")
worksheet = workbook.WorkSheets[0]

# Choose a cell range

***Based on <https://ironsoftware.com/docs/docs/>***

selected_range = worksheet["A2:A8"]

# Conduct an ascending sort on the range

***Based on <https://ironsoftware.com/docs/docs/>***

selected_range.SortAscending()

# Commit changes with the sorting applied

***Based on <https://ironsoftware.com/docs/docs/>***

workbook.Save()
```

## Modifying Formulas

Setting and recalculating Excel formulas is straightforward:

```python
# Assign a formula to a cell

***Based on <https://ironsoftware.com/docs/docs/>***

workSheet["A1"].Formula = "=SUM(A2:A10)"
# Retrieve and display the calculated value

***Based on <https://ironsoftware.com/docs/docs/>***

sum_ = workSheet["A1"].DecimalValue
```

## Benefits of Using IronXL for Python

IronXL for Python provides a user-friendly API that simplifies reading from and writing to Excel files. It eliminates the dependency on Microsoft Excel or Excel Interop for managing Excel documents, enhancing ease and efficiency.

## Licensing & Customer Support

**IronXL for Python** is freely available for development purposes.

For production use, [acquire a license here](https://ironsoftware.com/python/excel/licensing/). Trial licenses lasting 30 days are obtainable [here](https://ironsoftware.com/python/excel/trial-license).

Explore more code samples, tutorials, and detailed documentation about **IronXL for Python** at [this resource](https://ironsoftware.com/python/excel/).

For additional assistance and inquiries, feel free to [contact our support team](https://ironsoftware.com/live-chat-support).