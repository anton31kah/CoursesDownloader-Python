from datetime import datetime

import keyring
import requests
import lxml.html
from urllib3.exceptions import MaxRetryError

from AdvancedInput.MenuChooseItem import ask_yes_no_question
from Common.CommonFuncs import clear


class CoursesClient:
	__login_time = None
	session = None

	@classmethod
	def __create_session(cls):
		session = requests.session()

		while True:
			print("Establishing connection with courses")

			try:
				login = session.get("http://courses.finki.ukim.mk/login/index.php", allow_redirects=True)

			except (MaxRetryError, requests.exceptions.ConnectionError):
				print("Connection cannot be established")
				should_retry = ask_yes_no_question("Do you want to try again? [Y/N] ", None)
				if not should_retry:
					quit()
				else:
					clear()
					continue

			break

		print("Preparing CAS login")

		login_html = lxml.html.fromstring(login.text)
		hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
		login_data = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}

		login_data['username'] = '161555'

		login_data['password'] = keyring.get_password('https://cas.finki.ukim.mk/', login_data['username'])

		print("Logging into CAS")

		session.post(login.url, data=login_data)

		cls.__login_time = datetime.now()

		cls.session = session

	def __new__(cls):
		if not hasattr(cls, 'session') or not cls.__login_time:
			cls.__create_session()
			return

		curr_time = datetime.now()
		diff = curr_time - cls.__login_time
		diff_in_minutes = diff.seconds / 60

		if diff_in_minutes > 30:
			cls.__create_session()

	@classmethod
	def refresh(cls):
		cls.__create_session()
		return cls.session
