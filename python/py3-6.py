import smtplib
content =' i am so great'
mao=  'abisheik'
mail= smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('arjun.sayonetech','******')
conyen=f'Subject: {content}\n\n{content}'
mail.sendmail('arjun.sayonetech','shelson.sayonetech@gmail.com',conyen)
mail.close()