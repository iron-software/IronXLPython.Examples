from ironxl import *

def run():
    # Set a formula
    workSheet["A1"].Formula = "=SUM(A2:A10)"
    # Get the calculated value
    sum_ = workSheet["A1"].DecimalValue