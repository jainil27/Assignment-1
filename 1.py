ip = (input())                    #input function to take input from user
splitted_ip=ip.split()            # split function to slice the string and convert into a list
print(" ".join(list(set(splitted_ip))))   #join function to print it as a string again
                                          #set function to remove duplicates
