from Common.CommonFuncs import clear
from CoursesClient.CoursesClient import CoursesClient


class CoursesDownloaderBase:
	def __init__(self):
		self.course_link = None
		self.selected_section = None
		self.selected_links = []
		CoursesClient()

	def _download_selected_links(self):
		total_len = len(self.selected_links)

		if total_len == 1:
			self.selected_links[0].download()
		elif total_len > 1:
			for idx, link in enumerate(self.selected_links, 1):
				clear()
				print(f"Downloading {idx} / {total_len}")
				link.download(ambiguous=True)

			print(f"Downloaded {total_len} successfully")

