lines = []                  # an empty list
while True:                  # infinite loop
    line = input()           # accept a one line string  
    if line:                  # if a valid line is entered
        lines.append(line)    # add the line to list
    else:
        break                 # if not a valid line 
text = '\n'.join(lines)       # join the list 
print(text.upper())         # print list in uppercase
