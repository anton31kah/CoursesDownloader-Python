import re

from Common.CommonFuncs import CommonFuncs
from SpecialActions.ActionState import ActionState


class BaseAction:
	type = "Base"
	state = None
	children = ("Back", "Open", "Copy", "Exit", "Quit")

	@classmethod
	def handle(cls, input_string):
		words = "|".join(cls.children)
		actions_found = re.findall(rf"\b(?:{words})\b", input_string, re.IGNORECASE)
		if actions_found:
			action_class_name = actions_found[0].title() + "Action"

			action_class = CommonFuncs.class_for_name(f"SpecialActions.{action_class_name}", action_class_name)
			action_class.handle(input_string)
			return cls

		cls.state = ActionState.not_found
		return cls

	@classmethod
	def set_action_idx_pointer(cls, level):
		pass
