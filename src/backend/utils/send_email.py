from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
import smtplib 

subject = 'Reminder'
body = """
<html>
<head>
</head>
<body>
    <p>Dear Patient,</p>
    <p><strong style="color: red;">Tomorrow is your scheduled treatment day, please make sure to attend.</strong></p>
    <p>We look forward to seeing you to continue your treatment process.</p>
    <p>If you have any questions or need further information, please feel free to contact us.</p>
</body>
</html>
"""

def send_email(subject, body, target_email):
    sender = 'notification.pumpkin.penguin@gmail.com'
    password = 'xamxmmdkjjsefzrb'
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 
    smtp.starttls() 
    smtp.login(sender,password)

    msg = MIMEMultipart() 
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'html'))

    smtp.sendmail(from_addr=sender, 
				to_addrs= target_email, msg=msg.as_string()) 
    smtp.quit()
    