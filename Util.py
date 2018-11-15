import smtplib
import os
from datetime import datetime


def report_error(error_message):
    header = 'From: Bot runtime\r\n'
    header += 'To: Admin Email\r\n'
    header += 'Subject: HottestCityBot query on %s failed\r\n' % str(datetime.today())

    message = "Weather query for %s failed with an exception.\n %s" % (str(datetime.today()), error_message)
    message = header + message

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()

    email_address = os.getenv("email_address")
    email_password = os.getenv("email_password")

    if not (email_address and email_password):
        return

    server.login(email_address, email_password)
    server.sendmail("hottestcitytwitter@gmail.com", "hottestcitytwitter@gmail.com", message)
    server.quit()