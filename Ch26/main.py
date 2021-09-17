import smtplib

mySMTP = smtplib.SMTP('smtp.gmail.com',587)
mySMTP.ehlo()
mySMTP.starttls()
mySMTP.login('moneychien20639@gmail.com','arthur108306019')
status = mySMTP.sendmail('moneychien20639@gmail.com',
                         'moneychien20639@gmail.com',
                         'Subject:Hello shark\nMessage from python')
print(status)
print(mySMTP.quit())