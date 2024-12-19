from ironxl import *

def run():
    # Access cell B1 in the worksheet
    cell = workSheet["B1"]
    # Read the value of the cell as a string
    value = cell.StringValue
    print(value)
    # Write a new value to the cell
    cell.Value = "10.3289"
    print(cell.StringValue)