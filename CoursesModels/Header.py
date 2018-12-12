import re


class Header:
	def __init__(self, name="", order="", anchor_id=""):
		self.name = name
		tag_order = re.findall(r"\d+", order)
		if tag_order:
			self.order = tag_order[0]
		self.anchor_id = anchor_id

	def __repr__(self):
		return f"Header(name={self.name}, order={self.order}, anchor_id={self.anchor_id})"

	def __str__(self):
		return self.name

	def __eq__(self, other):
		return (
				isinstance(other, Header) and
				self.name == other.name
		)
