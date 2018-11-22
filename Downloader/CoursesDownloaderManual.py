from AdvancedInput.MenuChooseItem import ask_input_for_item_from_list, ask_input_for_items_from_list
from AdvancedInput.MenuChooseItem import ask_yes_no_question
from Common.BackWasPressed import BackWasPressed
from Common.CommonVars import CommonVars
from CoursesClient.SectionExtractor import extract_sections_for_course
from Downloader.CoursesDownloaderBase import CoursesDownloaderBase


class CoursesDownloaderManual(CoursesDownloaderBase):
	def __ask_for_course(self):
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

	def __count_specific_runner(self, count_specific_ask_method):
		self.__ask_for_course()
		self.__ask_for_section()
		count_specific_ask_method()
		self._download_selected_links()

	def __count_specific_runner_with_back(self, count_specific_ask_method):
		actions_to_perform = [
			self.__ask_for_course,
			self.__ask_for_section,
			count_specific_ask_method,
			self._download_selected_links
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
