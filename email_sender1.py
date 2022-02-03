import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('testingggg2002@gmail.com')
EMAIL_PASSWORD = os.environ.get('testing2002')

contacts = ['testingggg2002@gmail.com', 'sk9910570374@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Weather Notification'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'sk9910570374@gmail.com'

msg.set_content('ROM ROM BHAIYOOO!!! KUCH DHANG KA KAAM KRO.')

# msg.add_alternative("""\
# <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
#     </body>
# </html>
# """, subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)