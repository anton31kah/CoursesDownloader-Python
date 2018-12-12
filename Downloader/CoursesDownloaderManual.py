from AdvancedInput.MenuChooseItem import ask_input_for_item_from_list, ask_input_for_items_from_list
from AdvancedInput.MenuChooseItem import ask_yes_no_question
from Common.CommonVars import CommonVars
from CoursesClient.SectionExtractor import extract_sections_for_course
from Downloader.CoursesDownloaderBase import CoursesDownloaderBase
from SpecialActions.BaseAction import BaseAction


class CoursesDownloaderManual(CoursesDownloaderBase):
	@classmethod
	def __ask_for_course(cls):
		result = ask_input_for_item_from_list(CommonVars.courses, "course")
		if isinstance(result, BaseAction):
			return result
		CommonVars.course_link = result.url
		return CommonVars.course_link

	@classmethod
	def __ask_for_section(cls):
		extract_sections_for_course(CommonVars.course_link)
		result = ask_input_for_item_from_list(CommonVars.sections, "section")
		if isinstance(result, BaseAction):
			return result
		CommonVars.selected_section = result
		return CommonVars.selected_section

	@classmethod
	def __ask_for_one_link(cls):
		CommonVars.selected_links.clear()
		result = ask_input_for_item_from_list(CommonVars.selected_section, "file", "download")
		if isinstance(result, BaseAction):
			return result
		CommonVars.selected_links.append(result)
		return CommonVars.selected_links[0]

	@classmethod
	def __ask_for_multiple_links(cls):
		CommonVars.selected_links.clear()
		result = ask_input_for_items_from_list(CommonVars.selected_section, "files", "download")
		if isinstance(result, BaseAction):
			return result
		CommonVars.selected_links.extend(result)
		return CommonVars.selected_links

	@staticmethod
	def __ask_for_naming_method():
		choices_possible = [
			"Use the file name from the url (default behavior when downloading from browser)",
			"Use the file name that appears on courses (Recommended)"
		]
		result = ask_input_for_item_from_list(choices_possible, "choice", "choose")
		if isinstance(result, BaseAction):
			return result
		elif result == choices_possible[0]:
			CommonVars.using_name_from_courses_instead_of_name_from_url = False
		elif result == choices_possible[1]:
			CommonVars.using_name_from_courses_instead_of_name_from_url = True

		return result

	def __count_specific_runner(self, count_specific_ask_method):
		self.__ask_for_course()
		self.__ask_for_section()
		count_specific_ask_method()
		self.__ask_for_naming_method()
		self._download_selected_links()

	def __count_specific_runner_with_back(self, count_specific_ask_method):
		actions_to_perform = [
			self.__ask_for_course,
			self.__ask_for_section,
			count_specific_ask_method,
			self.__ask_for_naming_method,
			self._download_selected_links
		]

		current_action_idx = 0

		while True:
			current_action = actions_to_perform[current_action_idx]
			result = current_action()
			if isinstance(result, BaseAction):
				current_action_idx = result.set_action_idx_pointer(current_action_idx)
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
