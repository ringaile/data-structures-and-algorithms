"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# get all the unique outgoing numbers
outgoingcalls = set()
incomingcalls = set()
for item in calls:
	outgoingcalls.add(item[0])
	incomingcalls.add(item[1])

allTexts = set()
for item in texts:
	allTexts.add(item[0])
	allTexts.add(item[1])	

possibleTelemarketers = outgoingcalls - incomingcalls - allTexts

print("These numbers could be telemarketers: ")
print('\n'.join(sorted(set(possibleTelemarketers))))		

