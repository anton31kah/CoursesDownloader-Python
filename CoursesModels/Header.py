import re


class Header:
	def __init__(self, name="", order=""):
		self.name = name
		tag_order = re.findall(r"\d+", order)
		if tag_order:
			self.order = tag_order[0]

	def __repr__(self):
		return f"Header(name={self.name}, order={self.order})"

	def __str__(self):
		return self.name

	def __eq__(self, other):
		return (
				isinstance(other, Header) and
				self.name == other.name
		)
