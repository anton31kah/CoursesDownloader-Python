import re

from CoursesClient.CoursesClient import CoursesClient
from Common.CommonVars import CommonVars
from CoursesModels.Links.DownloadableLink import DownloadableLink


class FolderLink(DownloadableLink):
	folder_download_link = "http://courses.finki.ukim.mk/mod/folder/download_folder.php"

	def _get_and_save_file(self, filename):
		CoursesClient()
		folder_to_download_id = re.findall(r"\d+$", self.url)[0]
		folder_to_download_sesskey = CommonVars.sesskey
		download_folder_data = {
			'id': folder_to_download_id,
			'sesskey': folder_to_download_sesskey
		}
		folder_to_download = CoursesClient.session.post(self.folder_download_link, data=download_folder_data, stream=True)

		if not filename:
			filename = self._get_filename_from_headers(folder_to_download)

		super()._download_with_progress(filename, folder_to_download)

		return filename
