from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import smtplib 
import os

smtp = smtplib.SMTP('smtp.gmail.com', 587) 
smtp.ehlo() 
smtp.starttls() 
# smtp.login('YourMail@gmail.com', 'Your Password')
# password is not login password, is smtp password
smtp.login('zhengtonglin211@gmail.com','djafzpxctuhuxhnc')

msg = MIMEMultipart() 
msg['Subject'] = 'Reminder'
msg.attach(MIMEText('Dear patient_name, Your treatment is tomorrow. Best, XXX'))

to = ["1093840892@qq.com.com", "ucabtt1@ucl.ac.uk"] 
smtp.sendmail(from_addr="zhengtonglin211@gmail.com", 
			to_addrs=to, msg=msg.as_string()) 
smtp.quit()
