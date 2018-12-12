import pyperclip

from SpecialActions.OpenCopyBaseAction import OpenCopyBaseAction


class CopyAction(OpenCopyBaseAction):
	type = "Copy"
	method_to_use = pyperclip.copy

	@classmethod
	def handle(cls, input_string):
		super().handle(input_string)

	@classmethod
	def set_action_idx_pointer(cls, level):
		return super().set_action_idx_pointer(level)

	@classmethod
	def handle_multiple_links(cls, selected_links):
		# noinspection PyCallByClass
		cls.method_to_use("\n".join(map(lambda link: link.url, selected_links)))
