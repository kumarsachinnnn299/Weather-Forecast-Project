import smtplib, ssl
port=465
smtp_server = smtplib.SMTP_SSL("smtp.gmail.com",port)
sender_email = "testingggg2002@gmail.com"
receiver_email = "sk9910570374@gmail.com"
password ="testing2002"
message= "Hello darkness my old friend i've come to talk to you again."
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
server.quit()