# Working with Excel in Python Using IronXL

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***


This tutorial offers Python programmers a detailed guide on how to leverage the IronXL library for reading and modifying Microsoft Excel files.

IronXL is an extensive library for handling Excel files, compatible with multiple programming environments including [.NET](https://ironsoftware.com/csharp/excel/) and [Python](https://ironsoftware.com/python/excel/). This article specifically addresses the usage of IronXL in Python scripts for managing Excel data.

For instructions on handling Microsoft Excel files with .NET, please refer to this [guide](https://ironsoftware.com/csharp/excel/tutorials/how-to-read-excel-file-csharp/).

Using IronXL, Python developers can perform tasks involving Excel files efficiently and effortlessly.

<hr class="separator">

## Guide Overview

### Steps for Handling Excel Files in Python

1. Install the Python Library for Excel management
2. Open and read an Excel workbook
3. Generate a new Excel workbook in either CSV or XLSX format
4. Modify values within a cell range
5. Check the accuracy of the data in your spreadsheets
6. Utilize Entity Framework to output data

<hr class="separator">

## Detailed Instructions

### Step 1: Integrate IronXL into Your Python Environment

Begin by adding IronXL to your Python project as a dependency. You can do this using **pip**, the popular Python package manager. Run the command below in your terminal:

```shell
pip install ironxl
```

This command installs IronXL, making it ready for use in your projects. Note, IronXL for Python depends on the IronXL for .NET, so ensure you have [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) installed.

<hr class="separator">

### Step 2: Open an Excel Workbook

The `WorkBook` object in IronXL represents an Excel workbook. Open an Excel file with the `WorkBook.Load` method by specifying the file's path:

```python
# Open an existing Excel file

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

workbook = WorkBook.Load("Spreadsheets\\GDP.xlsx")
```

A `WorkBook` includes various `WorkSheet` entities, each corresponding to a sheet within the Excel file. Extract a specific sheet using `WorkBook.GetWorkSheet`:

```python
# Fetch a particular worksheet called 'GDPByCountry' from the workbook

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

workSheet = workBook.GetWorkSheet("GDPByCountry")
```

### Generating New Excel Files

You can create an Excel file by constructing a new `WorkBook`:

```python
# Instantiate a new Workbook in XLSX format

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

workBook = WorkBook(ExcelFileFormat.XLSX)
```

### Adding a Worksheet

Every `WorkBook` includes one or more `WorkSheet`s:

<div class="content-img-align-center">
  <a rel="nofollow" href="https://ironsoftware.com/img/tutorials/how-to-read-excel-file-csharp/work-book.png" target="_blank">
    <img src="https://ironsoftware.com/img/tutorials/how-to-read-excel-file-csharp/work-book.png" alt="A workbook with two worksheets displayed in Excel." class="img-responsive add-shadow img-margin" style="max-width:100%;">
  </a>
  <p class="content__image-caption">View of a workbook with two worksheets in Excel.</p>
</div>

To add a new worksheet, you would use `workbook.create_worksheet` and specify its name.

```python
workSheet = workBook.CreateWorkSheet("GDPByCountry")
```

### Manipulating Cell Values

#### Single Cell Editing

Access and edit the values in specific cells by retrieving the cell from a `WorkSheet`:

```python
# Open an existing workbook and access the default worksheet

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

workbook = WorkBook.Load("test.xlsx")
worksheet = workbook.DefaultWorkSheet

# Retrieve the cell at position B1

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

cell = worksheet["B1"]
```

Each cell is accessed through the `Cell` object in IronXL. It provides properties and methods for direct interaction with cell data.

```python
# Reading and updating a cell value in B1

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

cell = workSheet["B1"]
value = cell.StringValue
print(value)

# Change value in the same cell

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

cell.Value = "10.3289"
print(cell.StringValue)
```

#### Implementing Formulas

You can set cell formulas to carry out calculations or data transformations:

```python
# Define a range and apply a formula through each cell in the range

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

range_ = workSheet["D2:D101"]

# Applying formula across range

***Based on <https://ironsoftware.com/tutorials/how-to-read-excel-file/>***

for y in range(2, i):
    cell = workSheet[f"C{y}"]
    cell.Formula = f"=B{y}/B{i}"
```

## Conclusion

IronXL.Excel is a powerful, standalone Python library that facilitates reading and writing of numerous spreadsheet formats without needing Microsoft Excel installed. It achieves high performance and compatibility without relying on Interop.