import os
from email.message import EmailMessage
from dotenv import load_dotenv
import ssl
import smtplib
import schedule
import time



load_dotenv()
smtp_server = os.environ.get("SMTP_SERVER") # or smtp.gmail.com
smtp_port = os.environ.get("SMTP_PORT") # 465 
email_sender = os.environ.get("EMAIL_SENDER")
email_password = os.environ.get("EMAIL_PASSWORD")
email_receiver = 'emailreceiver@mail.com' # ['emailreceiver@mail.com', 'emailreceiver1@mail.com']
subject = "SUBJECT...."
body = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras luctus luctus erat quis tristique. Phasellus feugiat, nulla quis aliquam suscipit, libero felis lobortis metus, vel tempor ante magna id massa. Phasellus libero ligula, imperdiet a nunc a, consequat congue nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam lacinia orci neque, nec fringilla massa maximus eget. Cras sit amet placerat mauris, quis efficitur ligula. Nullam maximus dapibus lacus. Cras ornare dictum risus et egestas. Vivamus ut arcu efficitur, bibendum est maximus, vehicula ligula. Ut dictum odio eu lorem sollicitudin viverra. Quisque ultricies lorem non risus suscipit tempor. Fusce vitae augue vulputate, lobortis sapien sit amet, interdum dolor.
"""


def send_email():
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server,smtp_port, context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

# Program the sending of the mail...


schedule.every().second.do(send_email)
#secomd
#minute
#hour
#etc.....

while True:
    schedule.run_pending()
    time.sleep(1)
