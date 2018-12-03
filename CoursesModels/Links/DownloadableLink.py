from abc import ABC, abstractmethod

from clint.textui import progress

from Common.CommonFuncs import CommonFuncs
from Common.CommonVars import CommonVars
from CoursesModels.Links.FileTypeKnownNotKnownHelpers.FileTypeKnown import FileTypeKnown
from CoursesModels.Links.FileTypeKnownNotKnownHelpers.FileTypeNotKnown import FileTypeNotKnown
from CoursesModels.Links.Link import Link


class DownloadableLink(ABC, Link):
	def download(self, ambiguous=False):
		if not ambiguous:
			CommonFuncs.clear()
			print(f"Downloading {self.name}")

		if CommonVars.using_name_from_courses_instead_of_name_from_url:
			# old way
			filename = FileTypeNotKnown.prepare_filename_for_downloading(self.name)
			self._get_and_save_file(filename)
			filename = FileTypeNotKnown.handle_file_name_and_type_and_if_duplicate(filename)
		else:
			# new way
			filename = self._get_and_save_file(None)
			filename = FileTypeKnown.get_filename_without_path(filename)
			pass

		if not ambiguous:
			print(f"Downloaded {self.name} as {filename}")

	@staticmethod
	def _get_filename_from_headers(courses_response):
		return FileTypeKnown.get_filename_from_headers(courses_response)

	@abstractmethod
	def _get_and_save_file(self, filename):
		pass

	@staticmethod
	def _download_with_progress(filename, thing_to_download):
		with open(filename, 'wb') as f:
			total_length = int(thing_to_download.headers.get('content-length'))

			expected_size = (total_length / 1024) + 1
			for chunk in progress.bar(thing_to_download.iter_content(chunk_size=1024), expected_size=expected_size):
				if chunk:
					f.write(chunk)
					f.flush()
