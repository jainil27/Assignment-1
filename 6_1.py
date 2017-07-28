def reversee(l):
    nl=[]
    for i in range(len(l)-1,-1,-1):
        nl.append(l[i])
    return nl
    
l=input()
l=l.split()
new_list=reversee(l)
print(new_list)
