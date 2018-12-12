from Common.CommonFuncs import CommonFuncs
from Common.CommonVars import CommonVars
from CoursesClient.CoursesClient import CoursesClient


class CoursesDownloaderBase:
	def __init__(self):
		CoursesClient()

	@classmethod
	def _download_selected_links(cls):
		total_len = len(CommonVars.selected_links)

		if total_len == 1:
			CommonVars.selected_links[0].download()
		elif total_len > 1:
			downloaded_names = []

			for idx, link in enumerate(CommonVars.selected_links, 1):
				CommonFuncs.clear()
				print(f"Downloading {link.name} {idx} / {total_len}")
				downloaded_names.append(link.name)
				link.download(ambiguous=True)

			print(f"Downloaded {total_len} successfully")
			for i, downloaded_name in enumerate(downloaded_names, 1):
				print(f"{i} {downloaded_name}")
