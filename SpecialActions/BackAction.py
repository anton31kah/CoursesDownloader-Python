from AdvancedInput.MenuChooseItem import ask_yes_no_question
from Common.CommonVars import CommonVars
from SpecialActions.ActionState import ActionState
from SpecialActions.BaseAction import BaseAction


class BackAction(BaseAction):
	type = "Back"

	@classmethod
	def handle(cls, input_string):
		BaseAction.state = ActionState.not_found
		if 'back' in input_string.lower():
			confirm_message = (
				"I noticed that you entered back, which will return you one step back\n"
				"Is that the action you wanted to perform (answer no if it was entered by mistake)? [Y/N] "
			)
			is_yes = ask_yes_no_question(confirm_message, None)
			if is_yes:
				BaseAction.state = ActionState.found_and_handled
				past_states = list(CommonVars.chosen_items_till_now.keys())
				if past_states:
					CommonVars.chosen_items_till_now.pop(past_states[-1])

	@classmethod
	def set_action_idx_pointer(cls, level):
		return level - 1 if level > 0 else 0
