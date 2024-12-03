# Iterate through all rows with a value
for y in range(2, i):
    # Get the C cell
    cell = workSheet[f"C{y}"]
    # Set the formula for the Percentage of Total column
    cell.Formula = f"=B{y}/B{i}"