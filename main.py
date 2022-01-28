#/usr/bin/env python3
#####################
import requests
from bs4 import BeautifulSoup
import argparse
import time
import pyfiglet
import smtplib
from email.mime.text import MIMEText


banner = pyfiglet.figlet_format("PS5 Checker  ")
print(banner)
print('[*] PS5 Checker [*] ')
print('Coded By Eng Yazeed ')
print(" [*] instagram COMMPLICATED [*] ")
print("This script work for outlook smtp server please if your using another server feel free to chenge the code ")


class ps5:

	def __init__(self , email , password , person ):
		self.email = email
		self.password = password
		self.person = person

		

	def sendmail(self):
		s = smtplib.SMTP('smtp-mail.outlook.com' , 587)
		s.connect('smtp-mail.outlook.com' , 587)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.set_debuglevel(1)
		msg = MIMEText("""body""")
		sender = self.email
		recipients = self.person
		msg['Subject'] = "PS5 is avalible !!!! ,,,,  at https://la3eb.com/en-sa/playstation-5-digital-with-black-dualsense-p-CFI-1116B-ZCT1BLK"
		msg['From'] = sender
		msg['To'] = recipients
		s.login(self.email , self.password)
		s.sendmail(sender, recipients.split(','), msg.as_string())

	def la3eb(self):
		count = 0
		while True:
			count = count + 1
			time.sleep(60)
			r = requests.get('https://la3eb.com/en-sa/playstation-5-digital-with-black-dualsense-p-CFI-1116B-ZCT1BLK')
			soup = BeautifulSoup(r.text , 'lxml')
			a = soup.find("button" , class_="btn Product_addToButton__3IXtt")
			if 'Out of Stock' in r.text:

				print( 'PS5 still Not avalible ... ')
				print(count)

				print(f"[*] Reason ... {a.text} [*]")
				#self.sendmail()

			else:
				print('Yyyyyyyyyyo its now avalible')
				self.sendmail()

def get_args():
	parser = argparse.ArgumentParser(description='la3eb ps5 Checker ..')
	parser.add_argument('-e', '--email', dest="email", required=True, action='store', help='your email to auth with')
	parser.add_argument('-p', '--password', dest="password", required=True, action='store', help='password of email to auth')
	parser.add_argument('-P', '--pe', dest="person", required=True, action='store', help='The person you want to get email ')
	args = parser.parse_args()
	return args

args = get_args()
email = args.email
password = args.password
person = args.person

l = ps5(email,password, person)
l.la3eb()
