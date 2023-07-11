from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib

sender_email = 'koreadoctorkim@gmail.com'
sender_password = "lydckcsnxsihuoqv"
receiver_email = 'koreadoctorkim@gmail.com'

smtp_name = "smtp.gmail.com"
smtp_port = 587
msg = MIMEMultipart()

name = '김형규'
phone_number = '010-1234-5678'

title = f'공진단 비대면 진료 요청: {name}님'
body = f'''{name}님의 공진단 비대면 진료 요청이 있습니다.
전화번호: {phone_number}
감사합니다.'''

msg['Subject'] = title
msg['From'] = sender_email
msg['To'] = receiver_email

contentPart = MIMEText(body)
msg.attach(contentPart)

s=smtplib.SMTP(smtp_name , smtp_port)
s.starttls()
s.login(sender_email , sender_password)
s.sendmail(sender_email, receiver_email, msg.as_string())
s.close()