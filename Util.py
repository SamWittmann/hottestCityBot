import smtplib
import yaml
import logging
from datetime import datetime


def report_error():
    logger = logging.getLogger('HottestCityBot')

    header = 'From: Bot runtime\r\n'
    header += 'To: Admin Email\r\n'
    header += 'Subject: HottestCityBot query on %s failed\r\n\r\n' % str(datetime.today().date())

    message = "Weather query for %s failed with an exception.\r\n" % (str(datetime.today().date()))
    message += "Check the logs for detailed error output."
    message = header + message

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
    except Exception:
        logger.exception("Failed to send error report email: Could not connect to the mail server.")
        return

    config = yaml.safe_load(file('config.yml', 'r'))

    email_address = config.get("email_address")
    email_password = config.get("email_password")

    if not (email_address and email_password):
        return
    try:
        server.login(email_address, email_password)
        server.sendmail("hottestcitytwitter@gmail.com", "hottestcitytwitter@gmail.com", message)
        server.quit()
        logger.info("Sent error report to hottestcitytwitter@gmail.com")
    except Exception:
        logger.exception("Failed to send error report email: Could not login to email account")
