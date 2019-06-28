import re

n=input()
li=[]
li=n.split(" ")
t=len(li)
for i in range(t):
    
    li[i]=' '+li[i]+' '
    # print(li[i])
    emails = re.findall(r'[\D\s][0-9]{10}[\D\s]',li[i])
    # print(emails)
    for j in emails:
        print(re.findall(r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',j))