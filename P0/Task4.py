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
numberList = []
for item in calls:
	numberList.append(item[0])

numberList = list(dict.fromkeys(numberList))

# check if those numbers were in incoming list
for item in calls:
	if item[1] in numberList:
		numberList.remove(item[1])

# check if those numbers were in sms list
for item in texts:
	if item[0] in numberList:
		numberList.remove(item[0])
	if item[1] in numberList:
		numberList.remove(item[1])

print("These numbers could be telemarketers: ")
print('\n'.join(numberList))		

