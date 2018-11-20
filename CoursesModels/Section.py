from CoursesModels.Header import Header
from CoursesModels.Links.Link import Link


class Section:
	def __init__(self, header=None, links=None):
		if isinstance(header, Header):
			self.header = header
		elif isinstance(header, str):
			self.header = Header(header)
		else:
			self.header = Header()

		self.links = links if isinstance(links, list) else []

	def __repr__(self):
		links_repr = ""
		if self.links:
			links_repr = "\n" + "\n".join(map(lambda x: x.__repr__(), self.links)) + "\n"
		return f"Section(header={self.header.name}, urls={{{links_repr}}})"

	def __str__(self):
		return self.header.name

	def __eq__(self, other):
		return (
				isinstance(other, Section) and
				self.header == other.header and
				self.links == other.links
		)

	def __len__(self):
		return len(self.links)

	def __getitem__(self, key):
		if isinstance(key, str):
			return next(filter(lambda x: x.name == key or x.url == key, self.links))
		elif isinstance(key, int):
			return self.links[key]
		else:
			return None

	def __contains__(self, item):
		return (
				isinstance(item, Link) and
				item in self.links
		)
