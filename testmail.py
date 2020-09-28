#!/usr/bin/python3

import smtplib
import base64

filename = "temp.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'zigsta_1@yahoo.com'
reciever = 'nlangle6@uncc.edu'

marker = "AUNIQUEMARKER"

# Define the main headers.
part1 = """From: zigsta_1@yahoo.com
To: nlangle6@uncc.edu
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s

This is a test email to send an attachement.
--%s--

""" % (marker, marker)


# Define the attachment section
part2 = """
Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2

try:
   smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
   smtpObj.starttls()
   smtpObj.login('zigsta_1@yahoo.com', 'ylgynhreznfmurav')
   smtpObj.sendmail(sender, reciever, message)
   print("Successfully sent email")
except sException:
   print("Error: unable to send email")