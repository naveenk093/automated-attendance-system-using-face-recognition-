import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders

sender_email = 'naveenkumarsn093@gmail.com'
sender_password = 'yozjbrerhqpohmrb'
receiver_email = 'satyamrathod57@gmail.com'
subject = 'CSV file attachment'
body = 'Please find the attached CSV file.'

file_path = 'C:/Users/navee/Desktop/project/1/Attendance-System-using-Face-Recognition-main/Attendance.csv'
file_name = os.path.basename(file_path)

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = COMMASPACE.join([receiver_email])
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

with open(file_path, 'rb') as f:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
    msg.attach(part)

# Send the email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, receiver_email, msg.as_string())