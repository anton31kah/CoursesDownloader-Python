from AdvancedInput.MenuChooseItem import ask_yes_no_question
from Common.CommonVars import CommonVars
from SpecialActions.ActionState import ActionState
from SpecialActions.BaseAction import BaseAction


class OpenCopyBaseAction(BaseAction):
	type = "OpenCopyBase"
	method_to_use = None

	@classmethod
	def handle(cls, input_string):
		BaseAction.state = ActionState.not_found
		action_word = cls.type.lower()
		if action_word in input_string.lower():
			confirm_message = (
				f"I noticed that you entered {action_word}, which will {action_word} the last selection\n"
				"Is that the action you wanted to perform (answer no if it was entered by mistake)? [Y/N] "
			)
			is_yes = ask_yes_no_question(confirm_message, None)
			if is_yes:
				BaseAction.state = ActionState.found_and_handled
				stages_depth = len(CommonVars.chosen_items_till_now)
				if stages_depth == 0:
					cls.method_to_use("https://courses.finki.ukim.mk/")
				elif stages_depth == 1:
					cls.method_to_use(CommonVars.course_link)
				elif stages_depth == 2:
					anchor_id = CommonVars.selected_section.header.anchor_id
					cls.method_to_use(f"{CommonVars.course_link}#{anchor_id}")
				elif stages_depth == 3:
					cls.handle_multiple_links(CommonVars.selected_links)

	@classmethod
	def set_action_idx_pointer(cls, level):
		return level

	@classmethod
	def handle_multiple_links(cls, selected_links):
		pass
