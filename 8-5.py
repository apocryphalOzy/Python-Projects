'''
Write a program to read through the mail box data and when you
find line that starts with “From”, you will split
the line into words using the split function.
We are interested in who sent the message, which is the second word on
the From line.
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
You will parse the From line and print out the second word for each From line,
then you will also count the number of From (not From:) lines and print out a
count at the end
'''

finput = input('Enter file path, pweeze: ')
fhand = open(finput)
count = 0
for line in fhand:
    #strip new line
    line = line.rstrip()
    #put line in a list and assign it to words variable
    words = line.split()
    #if the list has the length of zero(empty) or the first
        # elements do not start with 'From', continue
    if len(words) == 0 or words[0] != 'From' : #guardian pattern
        continue
    #else count +1 to every line that does
    count = count +1
    print('This is the',count,'value')
    #else get first index element value and print to shell
    print(words[1])

print('There are a total of,',count,'values in this text file.')
