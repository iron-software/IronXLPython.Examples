# IronXLPython.Examples

Runnable Python examples for [IronXL for Python](https://ironsoftware.com/python/excel/?utm_source=github), an Excel library that reads, writes, and edits XLSX, XLS, CSV, and TSV files without Microsoft Office or COM Interop.

## Install

```bash
pip install ironxl
```

## Quickstart

```python
from ironxl import *

License.LicenseKey = "YOUR-LICENSE-KEY"

# Load an existing workbook and read a cell
workbook = WorkBook.Load("sample.xlsx")
worksheet = workbook.WorkSheets[0]
print(worksheet["A2"].Value)

# Indexing with a range string returns an iterable Range
for cell in worksheet["A2:B10"]:
    print(f"Cell {cell.AddressString} has value '{cell.Text}'")

# Write a value and save
worksheet["C1"].Value = "Updated"
workbook.SaveAs("updated.xlsx")
```

IronXL for Python wraps the .NET library, so **members keep their .NET PascalCase names** — `SaveAs`, not `save_as`, and `WorkSheets`, not `worksheets`. A snake_case attribute is a sign the call is wrong. Ranges are reached by **indexing** the worksheet with a range string; there is no `range()` method.

`WorkBook.Create(ExcelFileFormat.XLSX)` starts a new workbook and requires a license key, unlike loading, so set `License.LicenseKey` before creating.

## What's in this repo

Each folder contains a self-contained project with a `requirements.txt`. Run `pip install -r requirements.txt`, then `python program.py`:

- `get-started/` — license-key setup
- `quickstart/` — an end-to-end project scaffold with tests
- `tutorials/` — a longer walkthrough covering reading an Excel file end to end

## Common tasks covered

- Loading XLSX and XLS workbooks and selecting worksheets
- Reading cell values, text, and addresses across a range
- Creating new workbooks and worksheets, and setting document metadata
- Writing cell values and saving to XLSX, XLS, CSV, JSON, and XML
- Cell formulas with automatic recalculation, read back as `DecimalValue`
- Cell styling: borders, border types, and colours
- Sorting a range ascending or descending

## Platform support

Python 3.7 and above. Windows, macOS, and Linux. See the [documentation](https://ironsoftware.com/python/excel/docs/?utm_source=github) for environment-specific notes.

## Documentation and support

- Full documentation: [ironsoftware.com/python/excel/docs](https://ironsoftware.com/python/excel/docs/?utm_source=github)
- API reference: [ironsoftware.com/csharp/excel/object-reference/api](https://ironsoftware.com/csharp/excel/object-reference/api/?utm_source=github) — the Python package exposes the same members under their .NET names
- PyPI package: [pypi.org/project/ironxl](https://pypi.org/project/ironxl/)
- Issues with these examples: file directly on this repository
- Product support: [support@ironsoftware.com](mailto:support@ironsoftware.com)

## About

This repository is maintained by [Iron Software](https://ironsoftware.com/?utm_source=github). IronXL for Python is a commercial library — see [licensing](https://ironsoftware.com/python/excel/licensing/?utm_source=github) for terms and trial details.
