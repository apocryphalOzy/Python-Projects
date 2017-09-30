'''
Write a program to open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split function.

For each word, check to see if the word is already in a list.
If the word is not inthe list, add it to the list.

When the program completes, sort and print the resulting words in alphabetical
order.
'''

#file handle open file path
fhand = open(r'C:\romeo.txt')
#creates empty list
lst = list()

#for loop, split each line into a list
for line in fhand:
    #can use multiple modules on same line
    #strip newline and split(put string of words in list) lines, assigned to line
    line = line.rstrip().split()
    #nested for loop to take each element in line variable
        #and see if we find repeated words within our newly created lists
    #this finds repeated words within our lists(for each element in our list)
    
    for element in line:
        #first passover is empty 
        
        if element in lst:
            continue
        #since first passover is an empty list, we append(add) our line elements to
            #our list() module which occurs in our else statement
        #as we loop through our nested loop, we append only one of our line elements
            #Thus giving us only one element in our new list() module
        else:
            lst.append(element)
            
#then we will sort each element in our list alphabetically
lst.sort()
#print this to our shell
print(lst)
