class Link:
	def __init__(self, name="", url=""):
		self.name = name
		self.url = url

	def __repr__(self):
		return f"Link(name={self.name}, url={self.url})"

	def __str__(self):
		return self.name

	def __eq__(self, other):
		return (
				isinstance(other, Link) and
				self.name == other.name and
				self.url == other.url
		)
