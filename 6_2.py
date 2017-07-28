nl=[]
def reversee(l):
    temp=l[0]
    del l[0]
    if(len(l)>0):
        reversee(l)
    nl.append(temp)
    return nl
    
l=input()
l=l.split()
new_l=reversee(l)
print(new_l)
