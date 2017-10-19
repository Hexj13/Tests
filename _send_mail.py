# coding: utf-8

import smtplib
import sys
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import StringIO

from rootsLib.roots import TakeDate

pattern_name = '*_testing.py'

mydict = {
	'[95m': '<font color="maroon">',
	'[94m': '<font color="blue">',
	'[92m': '<font color="green">',
	'[93m': '<font color="red">',
	'[91m': '<font color="blue">',
	'[0m': '</font>',
	'[1m': '<font face="cursive">',
	'[4m': '<font face="cursive">'}

me = 'flexbbytestingplatform@gmail.com'
you = 'vl@flexbby.com'

err_msq_text = '<h3>' + 'Error message :' + '</h3>' + '<br>'
log_msq_text = '<h3>' + 'Log message :' + '</h3>' + '<br>'
pattern_name_text = '<h4>' + 'Pattern name: ' + '</h4>'
success_name_text = '<h4>' + 'Success Testing! ' + TakeDate.today + '</h4>' + '<br>'
end_text = '<br>' + '===================FINISH REPORT===================' + '<br>'
start_text = '===================START REPORT===================' + '<br>'

msg = MIMEMultipart()
msg['From'] = me
msg['To'] = you
msg['Subject'] = 'Test Report' + TakeDate.today

# SMTP-сервер
server = "smtp.gmail.com"
port = 25
user_name = "flexbbytestingplatform@gmail.com"
user_passwd = "Flexbby7415365"


# отправка
def sendmail():
	s = smtplib.SMTP(server, port)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(user_name, user_passwd)
	s.sendmail(me, you, msg.as_string())
	s.quit()


# class MyStream(StringIO):
# 	stdout = sys.stdout
#
# 	def write(self, *args, **kwargs):
# 		StringIO.write(self, )


class TestResults(unittest.TestResult):
	def startTest(self, test):
		self.io = io = StringIO()
		sys.stdout = io
		sys.stderr = io

	def addError(self, test, err):
		super(TestResults, self).addError(test, err)
		txt = start_text + err_msq_text + self._exc_info_to_string(err, test).replace('\n', '<br/>') + log_msq_text + \
		      self.io.getvalue().replace('\n', '<br/>') + pattern_name_text + pattern_name + end_text
		for k, v in mydict.items():
			txt = txt.replace(k, v)
		error = MIMEText(txt, 'html')
		msg.attach(error)
		sendmail()

	def addFailure(self, test, err):
		super(TestResults, self).addFailure(test, err)
		txt = start_text + err_msq_text + self._exc_info_to_string(err, test).replace('\n', '<br/>') + log_msq_text + \
		      self.io.getvalue().replace('\n', '<br/>') + pattern_name_text + pattern_name + end_text
		for k, v in mydict.items():
			txt = txt.replace(k, v)
		error = MIMEText(txt, 'html')
		msg.attach(error)
		sendmail()

if __name__ == '__main__':
	suite = unittest.TestSuite(
		unittest.TestLoader().discover('C:/Users/Operator/Desktop/Tests', pattern=pattern_name)
	)
	results = TestResults()
	suite.run(results)
