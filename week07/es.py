# Write a program that reads in a text file and outputs the number of e's it contains.
### Splitting the count of e's by CAPTIAL e's and small e's
# The program should take the filename from an argument on the command line.
# Author: Fiona Healy Donnelly

# moby dick text file: https://www.gutenberg.org/files/2701/old/moby10b.txt

with open ("moby-dick.txt", 'r') as f: # I want to read in the file only, I don't need to make ammendments
    book = f.read()
    num_total_chars = len(book)
    print('The total number of characters in Moby Dick is {}'.format(num_total_chars)) 
    counter_small_e = 0 
    counter_big_e = 0
    for char in book:
        if char == "e":
            counter_small_e +=1
        elif char == "E":
            counter_big_e += 1
    print("The total number of small e's is {} and the total number of captial E's is {}".format(counter_small_e,counter_big_e))