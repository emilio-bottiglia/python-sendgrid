

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, Subject, PlainTextContent, SendGridException
import csv

#store apikey as environment variable
PSWD = os.environ.get("API_KEY")

#open a csv file in the same folder containing names and email addresses
csvFile = open("email-list.csv", "r", newline="")
fileData = csv.reader(csvFile)
next(fileData) #skip csv file header
for name, email in fileData: #parse each line in csv file and capture name and email

    #format email message 
    message = Mail(
        from_email='your_email@you.com', #email you want to appear the message sent from
        to_emails=email, #addresses email from csv file
        subject=("Test email"),

        #message body
        plain_text_content=PlainTextContent(f'''Hello {name}, 
        
        this is a test email sent from my pc using python and sendGrid APIs'''))

    try:
        sg = SendGridAPIClient(PSWD)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))
csvFile.close()
