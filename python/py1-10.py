li=[]
##li.append(list(map(str, input().split())))
n=input()
li=n.split(' ')
l=len(li)
##print (li)
if(l==1 and li[0]==''):
    print(" Nobody likes This")
##    print("1")
elif(l==1):
##    print("12")
    print(str(li[0])+" likes This")
elif(l==2):
##    print("2")    
    print(str(li[0])+" and "+str(li[1])+" likes This")
elif(l==3):
##    print("3")
    print(str(li[0])+" , "+str(li[1]) +" and "+str(li[2])+" likes This")
else:
##    print("4")
    print(str(li[0])+" , "+str(li[1]) +" and "+str(l-2)+" others likes This")
