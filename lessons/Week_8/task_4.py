##
#  This program reads a file whose lines contain items and prices, like this:
#  item name 1: price1
#  item name 2: price2
#  ...
#  Each item name is terminated with a colon.
#  The program writes a file in which the items are left-aligned and the
#  prices are right-aligned. The last line has the total of the prices.
#

from os.path import exists

# Prompt for the input and output file names.
input_filename = input("Input file: ")
output_filename = input("Output file: ")

# Check if the input file exists
if not exists(input_filename):
    print(f"ERROR: {input_filename} does not exist.")
    exit(0)

# Read the file contents
with open(input_filename) as f:
    input_lines = f.readlines()

# Make sure that the list is not empty
if len(input_lines) == 0:
    print(f"ERROR: {input_filename} is empty.")
    exit(0)

# Write the file
with open(output_filename, "w") as f:
    total, items = 0.0, 0

    for line in input_lines:
        # Make sure there is a colon in the input line, otherwise skip the line.
        if ":" not in line :
            continue

        # Split the record at the colon.
        parts = line.split(":")


        # Extract the two data fields. 
        item, price = parts[0], parts[1].strip()
 
        # Check if the price is valid
        if not parts[1].isdigit():
            print(f"ERROR: Invalid digit '{price}'.")
            continue

        # Compute values
        total += price
        items += 1

        # Write the output.
        f.write("%-20s%10.2f\n" % (item, price))

    # Write the amount of items and the total
    f.write(f"\n{'Total':20s}{total:10.2f}\n")
    f.write(f"{'No of items':20s}{items:10d}\n")


