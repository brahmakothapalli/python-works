import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = "Email From Python"
msg['From'] = "QABABU Works"
msg['To'] = "qababu8@gmail.com"



server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

#connection.starttls()

server.login('qababu9@gmail.com', 'password')

server.send_message(msg)

server.quit()

# server.sendmail("qababuworks@gmail.com", "qababuworks@gmail.com", "sending email from Python")

print("Email sent successfully!")