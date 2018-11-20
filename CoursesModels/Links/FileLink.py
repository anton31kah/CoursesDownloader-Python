from CoursesClient.CoursesClient import CoursesClient
from CoursesModels.Links.DownloadableLink import DownloadableLink


class FileLink(DownloadableLink):
	def _get_and_save_file(self, filename):
		CoursesClient()
		file_to_download = CoursesClient.session.get(self.url, allow_redirects=True)

		with open(filename, 'wb') as f:
			f.write(file_to_download.content)
