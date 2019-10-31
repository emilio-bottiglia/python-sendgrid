import os #to rertrieve environment variable
import smtplib #to send email
import ssl #support for ssl
from email.message import EmailMessage #message formatting
import csv


#SendGrid parameters. Username and api key are stored as 
#environment variable and called by the system when needed
#to avoid credential exposure

#USERNAME = os.environ.get("USER_NAME")
#PASSWORD = os.environ.get("API_KEY")
mailServer = "smtp.sendgrid.net"
port = 465
username = "apikey"
sender = "boemilio@live.com"
#receiver = "ebottig@gmail.com"
#receiver1 = "ebottig2@ie.ibm.com"
pswd = "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"

#message formatting 
msg = EmailMessage()




#msg["To"] = "" 
#msg["Bcc"] = email


#name = "emilio"
msgBody = '''Hello {to},

this is a sample email

thanks
emilio'''




#Send email. Class SMTP manage connections to a SMTP server
secureContext = ssl.create_default_context()
server =  smtplib.SMTP_SSL(mailServer, port, context=secureContext)
server.login(username, pswd)
csvFile = open("email-list.csv", "r", newline="")
    #fileData = csv.reader(csvFile)
fileData = csv.reader(csvFile)
next(fileData) #skip header
for name, email in fileData:
    msg.set_content(msgBody.format(to=name))
    msg["Subject"] = "Test"
    msg["From"] = sender
    msg["To"] = email
    server.send_message(msg)
csvFile.close()
server.quit()
