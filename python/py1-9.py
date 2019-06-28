f=open("text.txt",'w')
print("enter text (press ' enter and ~' to exit)")
b=input()
while(b!='~'):
    
    f.write(b)
    f.write('\n')
    b=input()
f.close()
f=open("text.txt",'r')
li=[]
li=f.readlines()
##print (li)
dd=len(li)
print("no of lines :"+str(dd))
s=""
for i in li:
##    print(i)
    s+=i+' '
bi=[]

bi=s.split(' ')
l=len(bi)

print("no of character is :"+str(len(s)-(2*dd)))
print("no of words"+str(l-1))

f.close()
