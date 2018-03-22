import smtplib

from email.mime.multipart import MIMEMultipart
from check_email import check_email
from datetime import datetime

def build_email(**kwargs): 

    msg = MIMEMultipart()
    msg['Subject'] = kwargs['subject']

    email_adds = open("email.address.txt")
    receiver = []

    for email in email_adds:
        check_email()
        receiver.append(email)

    email_adds.close()     

    msg['From'] = kwargs['sender']
    msg['To'] = ', '.join(destination)
    date = datetime.now()
    msg.preamble = f"Agora são [{date.hour} - {date.minutes}]\n\n"
   # body = "O café esta pronto!  Corre, se não vai acabar"
    msg.attach(MIMEtext(kwargs["body"], 'plain'))

    # Send the email via our own SMTP server.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(kwargs['sender'], kwargs['password'])

    server.sendmail(sender, destination, msg.as_string())
    server.quit()
