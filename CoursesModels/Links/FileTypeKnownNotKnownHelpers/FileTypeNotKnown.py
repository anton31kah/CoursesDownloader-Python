import mimetypes
import os

from magic import magic

from Common.CommonFuncs import CommonFuncs
from Common.CommonVars import CommonVars
from CoursesModels.Links.FileTypeKnownNotKnownHelpers.FileTypeKnownNotKnownCommon import \
	FileTypeKnownNotKnownCommon


class FileTypeNotKnown:
	@staticmethod
	def prepare_filename_for_downloading(filename):
		return FileTypeKnownNotKnownCommon.prepare_valid_file_path(filename)

	@staticmethod
	def handle_file_name_and_type_and_if_duplicate(filename):
		file_type_mime = FileTypeNotKnown._handle_cyrillic_filename(filename)
		file_type = mimetypes.guess_extension(file_type_mime)
		# file_type = re.sub("\w+/(\w+)", r"\g<1>", file_type)

		if not file_type:
			file_type = CommonVars.known_file_types[file_type_mime]

		if not file_type:
			file_type = ".unknown"

		new_filename = FileTypeKnownNotKnownCommon._handle_file_name_exists(filename, file_type)

		os.rename(filename, f"{new_filename}{file_type}")

		filename = f"{new_filename}{file_type}"
		filename = filename.replace(FileTypeKnownNotKnownCommon.default_location, "")

		return filename

	@staticmethod
	def _handle_cyrillic_filename(filename):
		transliterated_filename = CommonFuncs.transliterate_mk_to_en(filename, CommonVars.macedonian_to_english_chars)

		os.rename(filename, transliterated_filename)

		file_type_mime = magic.from_file(transliterated_filename, mime=True)

		os.rename(transliterated_filename, filename)

		return file_type_mime
