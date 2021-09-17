import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from_address = 'moneychien20639@gmail.com'
password = input('Password: ')
to_address_list = ['moneychien20639@gmail.com','oliviachien123@gmail.com']

with open('4910.jpg','rb') as f:
    mailContent = f.read()

message = MIMEImage(mailContent)

message['Content-Type'] = 'aplication/octet-stream'
message['Content-Disposition'] = 'attachment; filename="4910.jpg"'
message['Subject'] = 'Cool picture'
message['From'] = 'RD'
message['To'] = 'PD'

print(message)

mySMTP = smtplib.SMTP('smtp.gmail.com',587)
mySMTP.ehlo()
mySMTP.starttls()
mySMTP.login(from_address,password)
status = mySMTP.sendmail(from_address, to_address_list, message.as_string())

if status == {}:
    print('Mail sent !')

mySMTP.quit()