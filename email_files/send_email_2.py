import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


def build_send_email(**kwargs):

    msg = MIMEMultipart()
    msg['Subject'] = kwargs['subject']

    email_adds = open("email_address.txt")

    receivers = []

    for email in email_adds:

        email = str(email)

        if email.strip():
            # check_format_email.check_format_email(email)
            receivers.append(email)

    email_adds.close()

    msg['From'] = kwargs['sender']
    msg['To'] = ', '.join(receivers)
    date = datetime.now()
    msg.attach(MIMEText(f"Agora são [{date.hour}horas e {date.minute} minutos] e o seu amigo {kwargs['user']} está avisando: \n".encode(
        "utf-8"), 'plain', 'utf-8'))
    msg.attach(MIMEText(kwargs["body"].encode('utf-8'), 'plain', 'utf-8'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(kwargs['sender'], kwargs['passw'])

    server.sendmail(kwargs['sender'], receivers, msg.as_string())
    server.quit()
    
def main():
    build_send_email(subject="Cafe", sender="vicesabot@gmail.com", body="O café esta pronto!",
                     passw="vicentemito", user= "ninguem")

if __name__ == '__main__':
    main()
