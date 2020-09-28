import smtplib
import numpy as np
import pandas as pd
from emailFunc import CurTime
from emailFunc import sendEmail
from google_drive_downloader import GoogleDriveDownloader as gdd #pip install googledrivedownloader
PEOPLE = 0
PEOPLE_SUBJECT = 1
PEOPLE_BODY = 2
COMPANY = 3
COMPANY_SUBJECT = 4
COMPANY_BODY = 5
'''gdd.download_file_from_google_drive(file_id='1GsyLVVAE9cB10Dis5zI9O3TKyyGrj_Lp',
                        dest_path='./Email_List.csv',
                        unzip=False,
                        overwrite=True
                        )
emails = pd.read_csv("./Email_List.csv", sep = ',', header = None)
print(emails)'''
t = CurTime().start()

sender = 'zigsta_1@yahoo.com'
#receivers = ['hburges9@uncc.edu','nlangle6@uncc.edu', 'aozgundu@uncc.edu', 'bhollin8@uncc.edu', 'tfische4@uncc.edu', 'ashell6@uncc.edu']
#mail = smtplib.SMTP('smtp.gmail.com', 587)
try:
	while True:
		if  t.currentTime().weekday() == 0 and t.currentTime().hour == 0 and t.currentTime().minute == 0 and t.currentTime().second == 0:
			gdd.download_file_from_google_drive(
									file_id='1GsyLVVAE9cB10Dis5zI9O3TKyyGrj_Lp',
                                    dest_path='./Email_List.csv',
                                    unzip=False,
                                    overwrite=True
                                    )
			emails = pd.read_csv("./Email_List.csv", sep = ',', header = None)
			for i in range(1,emails.shape[1]):
				print(emails[i][PEOPLE])
				#print('{0}'.format(emails[i][1]))
				#print('{0}'.format(emails[i][2]))
				if emails[i][PEOPLE] != 'NaN':
					print(emails[i][PEOPLE])
					sendEmail(
						sender=sender,
				        receiver_list=[emails[i][PEOPLE]],
				        subject=emails[i][PEOPLE_SUBJECT],
				        html_body='<b>Google Drive Implementation Testing</b>',
				        plain_text_body='{0}'.format(emails[i][PEOPLE_BODY]),
				        login='zigsta_1@yahoo.com',
				        password='cwixvsqtzljggyzc',
				        smtpserver='smtp.mail.yahoo.com:587',
				        attachment="temp.txt"
				        )
				if emails[i][COMPANY] != 'NaN':
					print(emails[i][COMPANY])
					sendEmail(
						sender=sender,
				        receiver_list=[emails[i][COMPANY]],
				        subject=emails[i][COMPANY_SUBJECT],
				        html_body='<b>Google Drive Implementation Testing</b>',
				        plain_text_body='{0}'.format(emails[i][COMPANY_BODY]),
				        login='zigsta_1@yahoo.com',
				        password='cwixvsqtzljggyzc',
				        smtpserver='smtp.mail.yahoo.com:587',
				        attachment="temp.txt"                                                #should be resume.doc
				        )
	#t.stop()
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    t.stop()
    pass



