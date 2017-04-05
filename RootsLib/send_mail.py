# coding: utf-8

import smtplib
import unittest
from email.mime.text import MIMEText

# отправитель
from_who = 'flexbbytestingplatform@gmail.com'
# получатель
to = 'vl@flexbby.com'
# текст письма
text = 'Error in test'
# заголовок письма
subj = 'Error in test'
# SMTP-сервер
server = "smtp.gmail.com"
port = 25
user_name = "flexbbytestingplatform@gmail.com"
user_passwd = "Flexbby7415365"


# отправка
def sendmail(from_who, to, msg):
	s = smtplib.SMTP(server, port)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(user_name, user_passwd)
	s.sendmail(from_who, to, msg)
	s.quit()


class TestResults(unittest.TestResult):
	def addError(self, test, err):
		super(TestResults, self).addError(test, err)
		error = self._exc_info_to_string(err, test)
		sendmail(from_who, to, error)

	def addFailure(self, test, err):
		super(TestResults, self).addFailure(test, err)
		error = self._exc_info_to_string(err, test)
		sendmail(from_who, to, error)


if __name__ == '__main__':
	suite = unittest.TestSuite(
		unittest.TestLoader().discover(r'C:\Users\Operator\Desktop\Tests')
	)
	results = TestResults()
	suite.run(results)
