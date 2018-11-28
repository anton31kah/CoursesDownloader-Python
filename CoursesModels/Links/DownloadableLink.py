import mimetypes
import os
import os.path
import re
from abc import ABC, abstractmethod
from pathlib import Path

import magic

from Common.CommonVars import CommonVars
from Common.CommonFuncs import CommonFuncs
from CoursesModels.Links.Link import Link


class DownloadableLink(ABC, Link):
	valid_filename_regex = r"^[\w\-. ]+$"
	illegal_chars_regex = r"[^\w\-. ]"

	default_location = f"{Path.home()}\\Downloads\\"

	def download(self, ambiguous=False):
		if not ambiguous:
			CommonFuncs.clear()
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

		new_filename = self.handle_file_name_exists(filename, file_type)

		os.rename(filename, f"{new_filename}{file_type}")

		filename = f"{new_filename}{file_type}"
		filename = filename.replace(self.default_location, "")

		return filename

	@staticmethod
	def handle_cyrillic_filename(filename):
		transliterated_filename = CommonFuncs.transliterate_mk_to_en(filename, CommonVars.macedonian_to_english_chars)

		os.rename(filename, transliterated_filename)

		file_type_mime = magic.from_file(transliterated_filename, mime=True)

		os.rename(transliterated_filename, filename)

		return file_type_mime

	def _prepare_filename_for_downloading(self):
		filename = self.choose_naming()
		filename = re.sub(self.illegal_chars_regex, "_", filename)
		filename = self.default_location + filename
		return filename

	@staticmethod
	def handle_file_name_exists(filename, file_type):
		i = 1
		new_filename = filename
		while os.path.isfile(f"{new_filename}{file_type}"):
			new_filename = f"{filename}_{i}"
			i += 1

		return new_filename

	def choose_naming(self):
		if CommonVars.should_use_link_name_instead_of_name_from_url:
			return self.name
		else:
			return CommonFuncs.extract_filename_from_url(self.url)
