import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'testingggg2002@gmail.com'
# receiver_mail= 'reachshruti611@gmail.com'
EMAIL_PASSWORD = 'testing2002'
msg = EmailMessage()
msg['Subject'] = 'Weather Alert!!!'
msg['From'] = EMAIL_ADDRESS 
msg['To'] = ['sk9910570374@gmail.com']
msg.set_content('MAM YOU ARE JUST GREAT!!!!!!!')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
    smtp.send_message(msg)