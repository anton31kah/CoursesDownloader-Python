from AdvancedInput.MenuChooseItem import ask_yes_no_question
from SpecialActions.ActionState import ActionState
from SpecialActions.BaseAction import BaseAction


class QuitAction(BaseAction):
	type = "Quit"

	@classmethod
	def handle(cls, input_string):
		if 'quit' in input_string.lower():
			cls.state = ActionState.found_and_handled
			confirm_message = (
				"I noticed that you entered quit, which will quit the program\n"
				"Is that the action you wanted to perform (answer no if it was entered by mistake)? [Y/N] "
			)
			is_yes = ask_yes_no_question(confirm_message, None)
			if is_yes:
				raise SystemExit
				# return cls # well, the code back there won't exist so...

		cls.state = ActionState.not_found
		return cls

	@classmethod
	def set_action_idx_pointer(cls, level):
		pass
