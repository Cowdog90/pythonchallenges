import os
import csv
                                        #Set path

csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# Useful lists?

candidates = []                         #to get list of unique candidates
votes = []
percentages =[]


totalVotes = 0                          #Total Vote Counter


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # skip the header

    for row in csvreader:

        votes.append(row[2])            #Get a list of votes

        if row[2] not in candidates:
            candidates.append(row[2])   #Get a list of unique candidates

from collections import Counter
totalVotes = len(votes)                 #Get Total number of votes

x = Counter(votes)                      #Count votes by candidate

y = max(x,key=x.get)

for key in x:
    per = '{0:.2f}'.format(x[key] / totalVotes)
    percentages.append(per)


Title = 'Election Results'

print('Election Results')
print('----------------')

print('Total Votes: ',totalVotes)

ind = 0
for key in x:
 print(key,' : ',x[key], ' : ', percentages[ind])
 ind = ind + 1

print('Winner: ', y)


# Zip lists together
output_csv = zip(x,percentages)

# Set variable for output file
output_file = os.path.join("output.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)


    writer.writerow([Title])
    
    writer.writerows(output_csv)
    writer.writerow([y])