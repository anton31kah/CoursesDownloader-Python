import os
import re

from CoursesModels.Links.FileTypeKnownNotKnownHelpers.FileTypeKnownNotKnownCommon import \
	FileTypeKnownNotKnownCommon


class FileTypeKnown:
	@staticmethod
	def get_filename_from_headers(courses_response):
		content_headers = courses_response.headers['content-disposition']
		filename = re.findall("filename=(.+)", content_headers)[0]
		filename = filename.replace("\"", "")

		filename = FileTypeKnown.prepare_filename_for_downloading(filename)

		return filename

	@staticmethod
	def prepare_filename_for_downloading(filename):
		filename = FileTypeKnownNotKnownCommon.prepare_valid_file_path(filename)

		filename, file_type = os.path.splitext(filename)
		filename = FileTypeKnownNotKnownCommon._handle_file_name_exists(filename, file_type)
		filename = f"{filename}{file_type}"

		return filename

	@staticmethod
	def get_filename_without_path(filename):
		filename = filename.replace(FileTypeKnownNotKnownCommon.default_location, "")
		return filename
