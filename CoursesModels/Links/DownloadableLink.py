from abc import ABC, abstractmethod

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
