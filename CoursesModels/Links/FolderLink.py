import re

from CoursesClient.CoursesClient import CoursesClient
import Common.CommonVars as CommonVars
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
		folder_to_download = CoursesClient.session.post(self.folder_download_link, data=download_folder_data)

		with open(filename, 'wb') as f:
			f.write(folder_to_download.content)
