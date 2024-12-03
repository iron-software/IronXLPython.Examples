# Python Tutorial: Reading Excel Files

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***


This tutorial is designed to help Python developers learn how to use the IronXL library to manage Microsoft Excel documents effectively.

IronXL is a robust library for processing Excel files that supports multiple programming languages, including [Python](https://ironsoftware.com/python/excel/) and [.NET](https://ironsoftware.com/csharp/excel/). This tutorial specifically covers how to utilize IronXL within Python code to manipulate Excel files.

For guidance on handling Excel files in .NET applications, please see the dedicated tutorial [here](https://ironsoftware.com/csharp/excel/tutorials/how-to-read-excel-file-csharp/).

Using the IronXL library in Python makes it straightforward to interact with Excel files.

<hr class="separator">

<p class="main-content__segment-title">Overview</p>

<hr class="separator">

<p class="main-content__segment-title">Tutorial</p>

## Step 1: Incorporating IronXL into Your Python Project

To use the IronXL library in your Python projects, you should first install it via **pip**. Open your command prompt or terminal and run the following command:

```shell
pip install ironxl
```

This command installs IronXL and makes it ready for use in your project. Note that IronXL for Python leverages the .NET 6.0 framework as its foundation. Ensure the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) is installed on your system.

<hr class="separator">

## 2. Open an Excel Workbook

Excel documents are managed through the `WorkBook` class. To open an existing file, employ the `WorkBook.Load` method and specify the file's path:

```python
# Opening an existing Excel file

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

workbook = WorkBook.Load("Spreadsheets\\GDP.xlsx")
```

A `WorkBook` may contain several `WorkSheet` objects, each representing a sheet within the Excel file. To access a specific sheet:

```python
# Retrieving a worksheet from the workbook

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

workSheet = workBook.GetWorkSheet("GDPByCountry")
```

### Creating New Excel Documents

To create a fresh Excel file, instantiate a `WorkBook` object specifying the desired format:

```python
# Initializing a new Excel workbook

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

workBook = WorkBook(ExcelFileFormat.XLSX)
```

Use `ExcelFileFormat.XLS` for compatibility with older Excel versions (pre-95).

### Adding a Worksheet to a Document

A `WorkBook` in IronXL can hold multiple `WorkSheet` objects:

<div class="content-img-align-center">
  <a rel="nofollow" href="https://ironsoftware.com/img/tutorials/how-to-read-excel-file-csharp/work-book.png" target="_blank">
    <img src="https://ironsoftware.com/img/tutorials/how-to-read-excel-file-csharp/work-book.png" alt="Illustration of a workbook with two worksheets in Excel." class="img-responsive add-shadow img-margin" style="max-width:100%;">
  </a>
  <p class="content__image-caption">Illustration of a workbook containing two worksheets in Excel.</p>
</div>

To add a new worksheet:

```python
workSheet = workBook.CreateWorkSheet("GDPByCountry")
```

## 3. Manipulate Cell Values

### Modifying Single Cells

Cells are accessed directly by using their positions within the sheet:

```python
# Loading the default worksheet and accessing a specific cell

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

workbook = WorkBook.Load("test.xlsx")
worksheet = workbook.DefaultWorkSheet
cell = worksheet["B1"]
```

The `Cell` class provides properties and methods for reading and adjusting cell values directly:

```python
# Reading and updating values in a specific cell

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

cell = workSheet["B1"]
value = cell.StringValue
print(value)
cell.Value = "10.3289"
print(cell.StringValue)
```

### Handling Cell Ranges

Access multiple cells using the `Range` class, which represents a collection of cells:

```python
# Accessing a range of cells

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

range_ = workSheet["D2:D101"]
```

### Applying Formulas

To apply formulas in Excel cells, use the `Formula` property:

```python
# Applying a formula to cells

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

for y in range(2, i):
    cell = workSheet[f"C{y}"]
    cell.Formula = f"=B{y}/B{i}"
```

## Summary

IronXL.Excel is a powerful standalone Python library supporting numerous spreadsheet formats. It operates independently of Microsoft Excel and does not require [Microsoft Excel installation](https://products.office.com/en-us/excel).