"""
A simple utility app that will take lists from a file,
turn them into one list ignoring duplicates,
then export a new file with the new list.
"""
import re

#First, read the input as a string.
theBigList = open("input.txt", "r").read()

#Set it to all lowercase.
theBigList = theBigList.lower()

#Regex to find all the words, ignoring formatting and numbers and such.
theBigList = re.findall('[a-z]*[a-z]{2}', theBigList)

theFinalList = []

#Create a final list, ignoring all duplicates.
for i in theBigList:
	if i not in theFinalList:
		theFinalList.append(i)


#Alphabetize it.
theFinalList.sort()


#Turn it into a string
theOutputString = "["
for i in theFinalList:
	theOutputString += "\"" + i + "\", "
#Delete the extra comma and space, add the closing bracket.
theOutputString = theOutputString[:len(theOutputString)-2]
theOutputString += "]"


#Output to txt file.
with open("output.txt", 'w') as f:
	f.write(theOutputString)
	
	
