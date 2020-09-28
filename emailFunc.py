import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
from datetime import datetime
import pytz
from threading import Thread

def sendEmail(sender, 
			  receiver_list,
              subject,
              html_body,
              plain_text_body,
              login,
              password,
              smtpserver='smtp.gmail.com:587',
              cc_addr_list=None,
              attachment=None,
              from_name=None):
	try:
	    message=MIMEMultipart()

	    plain=MIMEText(plain_text_body,'plain')
	    html=MIMEText(html_body,'html') 

	    message.add_header('from',from_name)
	    message.add_header('to',','.join(receiver_list))
	    message.add_header('subject',subject)

	    if attachment != None:
	        attach_file=MIMEApplication(open(attachment,"rb").read())
	        attach_file.add_header('Content-Disposition', 'attachment', filename=attachment)
	        message.attach(attach_file)


	    message.attach(plain)
	    message.attach(html)

	    server = smtplib.SMTP(smtpserver)
	    server.starttls()
	    server.login(login,password)
	    server.sendmail(sender, receiver_list, message.as_string())
	    print("Mail Sent")
	    server.quit()
	except smtplib.SMTPException as e:
		print("Error: unable to send email: ")
		print(e)


if __name__ == '__main__':
	send_email(
		sender='zigsta_1@yahoo.com',
        receiver_list=["nlangle6@uncc.edu"],
        subject="Sending Attachement",
        html_body='html',
        plain_text_body='plain',
        login='zigsta_1@yahoo.com',
        password='sonbtlexoekoroan',
        smtpserver='smtp.mail.yahoo.com',
        attachment="temp.txt"
        )


class CurTime():
	def __init__(self, timezone = 'US/Eastern'):
		self.timezone = timezone
		self.stopped = False
	def currentTime(self):
		while True:
			if self.stopped:
				break
			return datetime.now(pytz.timezone('US/Eastern'))
	def start(self):
		# start the thread to read frames from the video stream
		self.t1 = Thread(target=self.currentTime, args=()).start()
		return self
	def stop(self):
		self.stopped = True