import os
import platform
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email as em
import diag_log
import system_info
from datetime import datetime


# SEND E-MAIL FUNCTION
def send_diagnostic_report():
    td5gServer = platform.uname()
    svrName = td5gServer.node
    root = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'TD5G Diagnostics')
    files = [f"system_report.txt",
             f"process_report.txt",
             f"drive_report.txt"]
    try:
        now = datetime.now()
        formatted_string = now.strftime("%m/%d/%Y %H:%M:%S")
        # logger.info('Setting GMAIL Server Information')
        port = 465
        smtp_server = 'smtp.gmail.com'
        sender_address = 's247.Diagnostics@gmail.com'
        sender_password = 'G2@2019!'
        recipients = ['MarkL@surveillance-247.com', 'VanessaS@surveillance-247.com', 'AnthonyM@surveillance-247.com']
        receiver_address = ''
        message = ''
        subject = f'TD5G Diagnostic Results {svrName}-- Date: {formatted_string}'
        body = 'See attached document for Diagnostic tool results. \n' \
               'Contact MarkL@surveillance-247.com with Issues'
        message = MIMEMultipart()
        message["From"] = sender_address
        message["To"] = receiver_address
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        for file in files:
            path = os.path.join(root, file)
            with open(path, "+rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            em.encoders.encode_base64(part)
            part.add_header(f'Content-Disposition', f'attachment; filename={file}')
            message.attach(part)
        text = message.as_string()
        context = ssl.create_default_context()
        i = 0
        while i < len(recipients):
            receiver_address = recipients[i]
            diag_log.logger.info('Beginning E-Mail Server Login / Sending E-Mail')
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                diag_log.logger.info('Logging into Mail Server')
                server.login(sender_address, sender_password)
                diag_log.logger.info('Sending E-Mail to: ' + str(receiver_address))
                server.sendmail(sender_address, receiver_address, text)
                diag_log.logger.info('E-Mail Sent to: ' + str(receiver_address))
            i += 1
    except PermissionError as e:
        diag_log.logger.debug(e)
