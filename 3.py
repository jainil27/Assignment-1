line=input()
a=0
d=0
for i in line:
    if(i.isalpha()):
        a=a+1
    elif(i.isdigit()):
        d=d+1
    else:
        pass                # writing else is compulsary and it cant be kept blank, so used pass
        
print('Letters: '+str(a)+' , Digits: '+str(d))
