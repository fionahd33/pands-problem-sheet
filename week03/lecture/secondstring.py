# This program reads in a string and outputs every second letter in reverse order
# Author Fiona Healy Donnelly

#Read in a string and reverse it
inputString = input("Please enter a string: ")
reverseString = (inputString[::-1])
print(reverseString)

# Output the string in reverse and only print every second letter
secondLetter = (reverseString[::2])
print(secondLetter)