import re
import lxml.html

from CoursesClient.CoursesClient import CoursesClient
from CoursesModels.Links.FileLink import FileLink
from CoursesModels.Links.FolderLink import FolderLink
from CoursesModels.Section import Section
import Common.CommonVars as CommonVars


def extract_sections_for_course(course_link):
	CoursesClient()
	course_page = CoursesClient.session.get(course_link, allow_redirects=True)
	CommonVars.sesskey = re.findall("(?<=sesskey=).{10}", course_page.text)[0]
	course_page_html = lxml.html.fromstring(course_page.text)
	headers_links = course_page_html.xpath(CommonVars.xpath_filter_a_h1_to_h6_with_folders)

	CommonVars.sections = []
	current_section = Section()
	CommonVars.sections.append(current_section)

	for header_link in headers_links:
		if header_link.tag.startswith("h"):
			current_section = Section(next(header_link.itertext()))
			CommonVars.sections.append(current_section)
		elif 'resource' in header_link.attrib['href']:  # header_link.tag.startswith("a")
			current_section.links.append(FileLink(next(header_link.itertext()), header_link.attrib['href']))
		elif 'folder' in header_link.attrib['href']:  # header_link.tag.startswith("a")
			current_section.links.append(FolderLink(next(header_link.itertext()), header_link.attrib['href']))

	CommonVars.sections = [section for section in CommonVars.sections if section.links]

	return CommonVars.sections
