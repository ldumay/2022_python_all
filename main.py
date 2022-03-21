#Source aide :
#
# Pour python Mail :
# - https://realpython.com/python-send-email/
# - https://www.youtube.com/watch?v=yOkhVTa2hT8
#
# Pour dotenv
# - https://pypi.org/project/python-dotenv/

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

import datetime
# import os
import smtplib
import ssl

if __name__ == '__main__':
    # take environment variables from .env.
    load_dotenv()

    # Date du jour
    today = datetime.datetime.now()

    #Configuration
    port = 587  # For TLS
    smtp_server = "mail.ldumay.fr"
    sender_email = "mailtester@ldumay.fr"
    receiver_email = "mailtester@ldumay.fr"
    sender_password = "wtNzzRyPtzpsC3oj"

    # Message
    message = MIMEMultipart()
    message["From"] = ""+sender_email+"sender_email"
    message["To"] = ""+receiver_email+""
    message["Subject"] = "Mail d'essai de "+str(today)
    body = "<html><h1>[Test]</h1><p>"+str(today)+"</p></html>"
    message.attach(MIMEText(body, 'html'))

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    print("[Python Mail] - Mail essai")
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(message["From"], sender_password)
    server.sendmail(message["From"], message["To"], message.as_string())
    server.quit()

    print("[Python Mail] - Mail envoyé !")