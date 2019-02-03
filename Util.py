import smtplib
import yaml
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

    config = yaml.safe_load(file('config.yml', 'r'))

    email_address = config.get("email_address")
    email_password = config.get("email_password")

    if not (email_address and email_password):
        return

    server.login(email_address, email_password)
    server.sendmail("hottestcitytwitter@gmail.com", "hottestcitytwitter@gmail.com", message)
    server.quit()