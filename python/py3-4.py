import urllib.request
import urllib.parse
import re
url='https://www.w3schools.com/xml/simple.xml'
req=urllib.request.urlopen(url)
resp=req.read()
##print(resp)
emails = re.findall(r'<name>(.*?)</name>',str(resp))
email = re.findall(r'<price>(.*?)</price>',str(resp))

for i in range (len(email)):
    print('name  :'+str(emails[i])+'\nprice   :'+str(email[i]))

