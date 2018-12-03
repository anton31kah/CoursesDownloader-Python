from Common.CommonFuncs import CommonFuncs
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
			downloaded_names = []

			for idx, link in enumerate(self.selected_links, 1):
				CommonFuncs.clear()
				print(f"Downloading {link.name} {idx} / {total_len}")
				downloaded_names.append(link.name)
				link.download(ambiguous=True)

			print(f"Downloaded {total_len} successfully")
			for i, downloaded_name in enumerate(downloaded_names, 1):
				print(f"{i} {downloaded_name}")
