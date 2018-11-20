class Header:
	def __init__(self, name=""):
		self.name = name

	def __repr__(self):
		return f"Header(name={self.name})"

	def __str__(self):
		return self.name

	def __eq__(self, other):
		return (
				isinstance(other, Header) and
				self.name == other.name
		)
