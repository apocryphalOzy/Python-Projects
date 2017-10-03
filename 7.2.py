finput = input('Enter file path: ')
fhand = open(finput)

#counter
count = 0
#accumulate
total = 0
for line in fhand:
    #strip newline character
    line = line.rstrip()
    #look for line that start with 'X-DSPAM-Confidence:'
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    #if line starts with that string, do this
    floaters = float(line[-6:])
    print(floaters)
    count = count + 1
    print(count)
    total = total + floaters
    #average confidence
    ASC = total/count
    print('ASC:',ASC)
