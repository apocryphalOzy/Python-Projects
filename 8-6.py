'''
Rewrite the program that prompts the user for a list of numbers and
prints out the maximum and minimum of the numbers at the end when the user
enters “done”.
Write the program to store the numbers the user enters in a list
and use the max() and min() functions to compute the maximum and minimum
numbers after the loop completes
'''

#create empty list
lst = list()
while True:
    
    #get user input
    inp = input('Enter a number: ')
    #if user enters 'done' break out of loop
    if inp == 'done': break
    
    #else append each value to lst variable
    else:
        try:
            #mutate lst by using append() function
            lst.append(int(inp))
            #shows elements within list
            print(lst)
            
        except Exception as exp:
            print(exp)
            
#get max element value in our list
print('Maximum list value is:', max(lst))
#get min element value in our list
print('Minimum list value is:',min(lst))

