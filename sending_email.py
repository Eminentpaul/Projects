from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Paulinus"
message["to"] = "eminentpaul2547@gmail.com"
message["subject"] = "My first Python Script for Email Sending"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user="oshipaulinus@gmail.com", password="paulinho254780")
    smtp.send_message(message)
    print("Sent Successfully")


