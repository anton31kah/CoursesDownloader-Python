from Common.BackWasPressed import BackWasPressed
from CoursesClient.CoursesClient import CoursesClient
from CoursesClient.SectionExtractor import extract_sections_for_course
from CoursesClient.CoursesDefiner import define_current_courses
from Common.CommonFuncs import clear
from Common.CommonVars import CommonVars
from AdvancedInput.MenuChooseItem import ask_input_for_item_from_list, ask_input_for_items_from_list
from AdvancedInput.MenuChooseItem import ask_yes_no_question


class CoursesDownloader:
	def __init__(self):
		self.course_link = None
		self.selected_section = None
		self.selected_links = []
		CoursesClient()
		define_current_courses()

	def __ask_for_course(self):
		define_current_courses()
		result = ask_input_for_item_from_list(CommonVars.courses, "course")
		if isinstance(result, BackWasPressed):
			return result
		self.course_link = result.url
		return self.course_link

	def __ask_for_section(self):
		extract_sections_for_course(self.course_link)
		result = ask_input_for_item_from_list(CommonVars.sections, "section")
		if isinstance(result, BackWasPressed):
			return result
		self.selected_section = result
		return self.selected_section

	def __ask_for_one_link(self):
		self.selected_links.clear()
		result = ask_input_for_item_from_list(self.selected_section, "file", "download")
		if isinstance(result, BackWasPressed):
			return result
		self.selected_links.append(result)
		return self.selected_links[0]

	def __ask_for_multiple_links(self):
		self.selected_links.clear()
		result = ask_input_for_items_from_list(self.selected_section, "files", "download")
		if isinstance(result, BackWasPressed):
			return result
		self.selected_links.extend(result)
		return self.selected_links

	def __download_selected_links(self):
		total_len = len(self.selected_links)

		if total_len == 1:
			self.selected_links[0].download()
		elif total_len > 1:
			for idx, link in enumerate(self.selected_links, 1):
				clear()
				print(f"Downloading {idx} / {total_len}")
				link.download(ambiguous=True)

			print(f"Downloaded {total_len} successfully")

	def __count_specific_runner(self, count_specific_ask_method):
		self.__ask_for_course()
		self.__ask_for_section()
		count_specific_ask_method()
		self.__download_selected_links()

	def __count_specific_runner_with_back(self, count_specific_ask_method):
		actions_to_perform = [
			self.__ask_for_course,
			self.__ask_for_section,
			count_specific_ask_method,
			self.__download_selected_links
		]

		current_action_idx = 0

		while True:
			current_action = actions_to_perform[current_action_idx]
			result = current_action()
			if isinstance(result, BackWasPressed):
				current_action_idx -= 1
				current_action_idx = max(0, current_action_idx)
			else:
				current_action_idx += 1
				if current_action_idx >= len(actions_to_perform):
					answer = ask_yes_no_question("Do you want to start again? [Y/N] ", None)
					if not answer:
						break
					else:
						CommonVars.chosen_items_till_now.clear()
						current_action_idx = 0
		pass

	def run_for_one_download(self):
		self.__count_specific_runner_with_back(self.__ask_for_one_link)

	def run_for_multiple_downloads(self):
		self.__count_specific_runner_with_back(self.__ask_for_multiple_links)


courses_downloader = CoursesDownloader()
courses_downloader.run_for_multiple_downloads()
