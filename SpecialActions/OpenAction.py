import webbrowser

from AdvancedInput.MenuChooseItem import ask_yes_no_question
from Common.CommonVars import CommonVars
from SpecialActions.ActionState import ActionState
from SpecialActions.BaseAction import BaseAction


class OpenAction(BaseAction):
	type = "Open"

	@classmethod
	def handle(cls, input_string):
		if 'open' in input_string.lower():
			cls.state = ActionState.found_and_handled
			confirm_message = (
				"I noticed that you entered open, which will open the last selection\n"
				"Is that the action you wanted to perform (answer no if it was entered by mistake)? [Y/N] "
			)
			is_yes = ask_yes_no_question(confirm_message, None)
			if is_yes:
				stages_depth = len(CommonVars.chosen_items_till_now)
				if stages_depth == 0:
					webbrowser.open_new_tab("https://courses.finki.ukim.mk/")
				elif stages_depth == 1:
					webbrowser.open_new_tab(CommonVars.course_link)
				elif stages_depth == 2:
					anchor_id = CommonVars.selected_section.header.anchor_id
					webbrowser.open_new_tab(f"{CommonVars.course_link}#{anchor_id}")
				elif stages_depth == 3:
					for link in CommonVars.selected_links:
						webbrowser.open_new_tab(link.url)

				return cls

		cls.state = ActionState.not_found
		return cls

	@classmethod
	def set_action_idx_pointer(cls, level):
		return level
