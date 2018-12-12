from SpecialActions.BaseAction import BaseAction
from SpecialActions.QuitAction import QuitAction


class ExitAction(BaseAction):
	type = "Exit"

	@classmethod
	def handle(cls, input_string):
		return QuitAction.handle(input_string)

	@classmethod
	def set_action_idx_pointer(cls, level):
		return QuitAction.set_action_idx_pointer(level)
