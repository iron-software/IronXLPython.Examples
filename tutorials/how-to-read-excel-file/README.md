# Python Read Excel File Tutorial

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***


This article walks Python developers through the steps of leveraging the IronXL library for reading and manipulating Microsoft Excel documents.

IronXL is an extensive Excel file handling library that supports a variety of programming languages, including [.NET](https://ironsoftware.com/csharp/excel/) and [Python](https://ironsoftware.com/python/excel/). This guide zeroes in on employing IronXL within Python scripts to access and modify Microsoft Excel documents.

For guidance on managing Microsoft Excel documents within .NET applications, please see this detailed guide [here](https://ironsoftware.com/csharp/excel/tutorials/how-to-read-excel-file-csharp/).

With Python, using the IronXL for Python software library makes handling Excel files straightforward.

<hr class="separator">

<p class="main-content__segment-title">Overview</p>

<hr class="separator">

<p class="main-content__segment-title">Tutorial</p>

## Step 1: Incorporating IronXL into Your Python Project

To add the IronXL library to your Python project, install it as a dependency with the **pip** package manager. Simply run the following command in your terminal:

```shell
pip install ironxl
```

This command ensures the IronXL library is downloaded and made ready for use in your project.

IronXL for Python is built on the IronXL .NET library, specifically targeting .NET 6.0. Make sure you have the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) installed on your computer to use IronXL for Python effectively.

<hr class="separator">

## Step 2: Opening an Excel Workbook

The `WorkBook` class in IronXL represents an Excel workbook. To open an Excel file, utilize the `WorkBook.Load` method while providing the file's path.

```python
# Load an existing Excel file

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

workbook = WorkBook.Load("Spreadsheets\\GDP.xlsx")
```

A `WorkBook` may contain several `WorkSheet` objects, each representing a sheet in the Excel workbook. Access a specific worksheet with the `WorkBook.GetWorkSheet` method.

```python
# Assuming workbook is a loaded WorkBook instance

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

workSheet = workBook.GetWorkSheet("GDPByCountry")
```

### Creating New Excel Documents

To craft a new Excel file, instantiate a `WorkBook` object specifying the desired Excel format.

```python
# Instantiate a new WorkBook in Excel format XLSX

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

workBook = WorkBook(ExcelFileFormat.XLSX)
```

Note: Use the `ExcelFileFormat.XLS` for compatibility with Microsoft Excel 95 and earlier versions.

### Adding a Worksheet to an Excel Workbook

IronXL allows you to manage multiple worksheets per workbook.

<div class="content-img-align-center">
  <a rel="nofollow" href="https://ironsoftware.com/img/tutorials/how-to-read-excel-file-csharp/work-book.png" target="_blank">
    <img src="https://ironsoftware.com/img/tutorials/how-to-read-excel-file-csharp/work-book.png" alt="This is how one workbook with two worksheets looks in Excel." class="img-responsive add-shadow img-margin" style="max-width:100%;">
  </a>
  <p class="content__image-caption">This is how one workbook with two worksheets looks in Excel.</p>
</div>

To add a new worksheet, use the `WorkBook.CreateWorkSheet` method.

```python
workSheet = workBook.CreateWorkSheet("GDPByCountry")
```

## Step 3: Accessing Cell Values

### Reading and Editing a Single Cell

To manipulate values in specific cells, first, retrieve the cell from its corresponding `WorkSheet`.

```python
# Load an existing spreadsheet

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

workbook = WorkBook.Load("test.xlsx")
worksheet = workbook.DefaultWorkSheet

# Access cell at position B1

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

cell = worksheet["B1"]
```

Each `WorkSheet` maintains a collection of `Cell` objects representing each cell in the worksheet. Here we access a cell using standard array indexing.

Here's how you can read and then write data to a cell:

```python
# Accessing, reading, and writing to cell B1

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

cell = workSheet["B1"]
value = cell.StringValue
print(value)

# Modifying the value in cell B1

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

cell.Value = "10.3289"
print(cell.StringValue)
```

### Reading and Writing Multiple Cells

The `Range` class encapsulates a collection of `Cell` objects, representing a block of cells in an Excel sheet. Access cell ranges using the string indexer on a `WorkSheet`.

```python
# Select a range of cells

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

range_ = workSheet["D2:D101"]
```

### Integrating Formulas into Cells

You can set formulas in cells using the `Formula` property. The following example demonstrates setting a formula in each cell in a column to calculate percentages.

```python
# Apply formulas across a range of cells

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

for y in range(2, i):
    cell = workSheet[f"C{y}"]
    cell.Formula = f"=B{y}/B{i}"
```

## Summary

IronXL.Excel is a standalone Python library that supports reading a variety of spreadsheet formats. It does not necessitate the presence of [Microsoft Excel](https://products.office.com/en-us/excel) on your system nor relies on Interop.