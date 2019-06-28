import re

n=input()
emails = re.findall(r'[\w\.-]+@[\w\.-]+',n)
if(emails):
    print('valid')
else:
    print("invalid")
