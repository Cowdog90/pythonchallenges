# Import Modules

import csv
import os

# Set path

csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# Useful lists?

date = []
Pnl = []
Change = []
Index = []

# Read in CSV file

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)  # skip the header
    months = 0 # Counter for number of months.
    totalPnl = 0 # Running total of profits and losses
    lastValue = 867884 # The starting point to track average change



    for row in csvreader:
        months = months + 1                     # Count the next month
        totalPnl = totalPnl + int(row[1])       # Total up Profit and Loss
        thisMonth = int(row[1])                 # Get this months PnL
        Change.append(thisMonth-lastValue)      # Add the change in monthly PnL to the Change list.
        Index.append(row[0])

        lastValue = thisMonth                   # This month's value becomes last value.

        max_value = max(Change)                 # Find MAX in Change
        max_index = Change.index(max(Change))
        min_value = min(Change)                 # find MIN in Change
        records = (len(Change)-1)               # get length of Change list
        min_index = Change.index(min(Change))


    avg_value = sum(Change) / (records)         # Calculate average monthly change


    print('Financial Analysis')
    print('-----------------------')

    print('Months: ',months)
    print('Total PnL :' ,totalPnl)
    print('Average Change :',avg_value)

    print('Greatest Increase :',(Index [max_index]),max_value)

    print('Greatest Decrease :',(Index [min_index]), min_value)

    a = ('Financial Analysis')
    b = ('-----------------------')

    c = ('Months: ',months)
    d = ('Total PnL :' ,totalPnl)
    e = ('Average Change :',avg_value)

    f = ('Greatest Increase :',(Index [max_index]),max_value)

    g = ('Greatest Decrease :',(Index [min_index]), min_value)



# Set variable for output file
output_file = os.path.join("pyBankOut.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)


    writer.writerow([a])
    writer.writerow([b])
    writer.writerow(c)
    writer.writerow(d)
    writer.writerow(e)
    writer.writerow(f)
    writer.writerow(g)

