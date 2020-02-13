"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


#get all unique phone numbers using set 
numberList = []

for item in calls:
	numberList.append(item[0])
	numberList.append(item[1])

#dictionary for each phone number and seconds spent
secondsOnPhone = {}
for number in numberList:
	seconds = 0
	for item in calls:
		if number == item[0]:
			seconds += int(item[3])
		if number == item[1]:
			seconds += int(item[3])
	secondsOnPhone[number] = seconds

# get the max value 
longest = max(zip(secondsOnPhone.values(), secondsOnPhone.keys())) 		

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(longest[1], longest[0]))
