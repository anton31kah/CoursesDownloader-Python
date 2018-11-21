import mimetypes
import os
import re
from abc import ABC, abstractmethod
from pathlib import Path

import magic

from Common.CommonVars import CommonVars
from Common.CommonFuncs import clear, transliterate_mk_to_en
from CoursesModels.Links.Link import Link


class DownloadableLink(ABC, Link):
	valid_filename_regex = r"^[\w\-. ]+$"
	illegal_chars_regex = r"[^\w\-. ]"

	default_location = f"{Path.home()}\\Downloads\\"

	def download(self, ambiguous=False):
		if not ambiguous:
			clear()
			print(f"Downloading {self.name}")

		filename = self._prepare_filename_for_downloading()

		self._get_and_save_file(filename)

		filename = self.handle_file_name_and_type(filename)

		if not ambiguous:
			print(f"Downloaded {self.name} as {filename}")

	@abstractmethod
	def _get_and_save_file(self, filename):
		pass

	def handle_file_name_and_type(self, filename):
		file_type_mime = self.handle_cyrillic_filename(filename)
		file_type = mimetypes.guess_extension(file_type_mime)
		# file_type = re.sub("\w+/(\w+)", r"\g<1>", file_type)

		if not file_type:
			file_type = CommonVars.known_file_types[file_type_mime]

		if not file_type:
			file_type = ".unknown"

		os.rename(filename, f"{filename}{file_type}")

		filename = f"{filename}{file_type}"
		filename = filename.replace(self.default_location, "")

		return filename

	@staticmethod
	def handle_cyrillic_filename(filename):
		transliterated_filename = transliterate_mk_to_en(filename, CommonVars.macedonian_to_english_chars)

		os.rename(filename, transliterated_filename)

		file_type_mime = magic.from_file(transliterated_filename, mime=True)

		os.rename(transliterated_filename, filename)

		return file_type_mime

	def _prepare_filename_for_downloading(self):
		filename = re.sub(self.illegal_chars_regex, "_", self.name)
		filename = self.default_location + filename
		return filename
