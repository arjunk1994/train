n=input()
li=[]
li=n
s=''
for i in li:
    if (i!='@'):
        s+=i
    else:
        break
if(s.isalpha()):
    print(s)
else:
    print("error in user name ")
            
