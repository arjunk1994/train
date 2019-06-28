n=input()
li=[]
li=n.split(',')
li.sort()
print(li)
s=''
for i in li:
    s+=i+', '
print(s)
