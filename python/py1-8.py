n=input()
li=[]
li=n.split(' ')
li.sort()
f=0
for i in li:
    if int(i)%2!=0:
        print(i)
        break

        
