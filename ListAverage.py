#make a program to compute average using a list

myList = list()

#start loop
while True:
    #get input from user
    inp = input('Enter a number: ')
    #break when 'done'
    if inp == 'done': break
    else:
        try:
            #append items to list
            myList.append(float(inp))
        except Exception as exc:
            print(exc)

    print('The average number input is:',sum(myList)/len(myList))
print('What shall I do next, human?')
