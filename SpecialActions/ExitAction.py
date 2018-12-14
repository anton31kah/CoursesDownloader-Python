from SpecialActions.BaseAction import BaseAction
from SpecialActions.QuitAction import QuitAction


class ExitAction(BaseAction):
	type = "Exit"

	@classmethod
	def handle(cls, input_string):
		QuitAction.handle(input_string)

	@classmethod
	def set_action_idx_pointer(cls, level):
		QuitAction.set_action_idx_pointer(level)
