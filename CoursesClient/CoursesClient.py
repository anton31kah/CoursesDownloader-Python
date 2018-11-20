from datetime import datetime

import keyring
import requests
import lxml.html


class CoursesClient:
	__login_time = None
	session = None

	@classmethod
	def __create_session(cls):
		session = requests.session()

		print("Establishing connection with courses")

		login = session.get("http://courses.finki.ukim.mk/login/index.php", allow_redirects=True)

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
