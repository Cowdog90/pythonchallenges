import os
import csv

csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# Useful lists?

date = []
Pnl = []
Change = []



with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # skip the header
    months = 0
    totalPnl = 0
    lastValue = 867884



    for row in csvreader:
        months = months + 1
        totalPnl = totalPnl + int(row[1])
        thisMonth = int(row[1])
        Change.append(thisMonth-lastValue)

        #print(lastValue, thisMonth,Change)
        lastValue = thisMonth

        max_value = max(Change)
        min_value = min(Change)
        records = (len(Change)-1)



    avg_value = sum(Change) / (records)



    print(months)
    print(totalPnl)
    print(avg_value)

    print(max_value)
    print(min_value)







