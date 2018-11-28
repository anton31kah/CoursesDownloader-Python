from CoursesModels.Links.CourseLink import CourseLink


class CommonVars:
	courses = []

	sections = []

	chosen_items_till_now = {}

	sesskey = None

	using_name_from_courses_instead_of_name_from_url = True

	known_file_types = {
		'application/pdf': '.pdf',
		'application/msword': '.doc',
		'application/vnd.openxmlformats-officedocument.wordprocessingml.document': '.docx',
		'application/vnd.openxmlformats-officedocument.presentationml.presentation': '.pptx',
		'application/zip': '.zip',
		'application/x-rar': '.rar',
		'image/jpeg': '.jpg',
		'image/png': '.png',
	}

	xpath_filter_a = "//a[starts-with(@href, 'http://courses.finki.ukim.mk/mod/resource/view.php?id=')]"
	xpath_filter_a_h1_to_h6 = (
		"//*[self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6 or self::a["
		"starts-with(@href, 'http://courses.finki.ukim.mk/mod/resource/view.php?id=')]] "
	)
	xpath_filter_a_h1_to_h6_with_folders = (
		"//*[self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6 "
		"or self::a[starts-with(@href, "
		"'http://courses.finki.ukim.mk/mod/resource/view.php?id=') or starts-with("
		"@href, 'http://courses.finki.ukim.mk/mod/folder/view.php?id=')]] "
	)

	macedonian_to_english_chars = {
		"А": "A", "а": "a",
		"Б": "B", "б": "b",
		"В": "V", "в": "v",
		"Г": "G", "г": "g",
		"Д": "D", "д": "d",
		"Ѓ": "Gj", "ѓ": "gj",
		"Е": "E", "е": "e",
		"Ж": "Zh", "ж": "zh",
		"З": "Z", "з": "z",
		"Ѕ": "Dz", "ѕ": "dz",
		"И": "I", "и": "i",
		"Ј": "J", "ј": "j",
		"К": "K", "к": "k",
		"Л": "L", "л": "l",
		"Љ": "Lj", "љ": "lj",
		"М": "M", "м": "m",
		"Н": "N", "н": "n",
		"Њ": "Nj", "њ": "nj",
		"О": "O", "о": "o",
		"П": "P", "п": "p",
		"Р": "R", "р": "r",
		"С": "S", "с": "s",
		"Т": "T", "т": "t",
		"Ќ": "Kj", "ќ": "kj",
		"У": "U", "у": "u",
		"Ф": "F", "ф": "f",
		"Х": "H", "х": "h",
		"Ц": "C", "ц": "c",
		"Ч": "Ch", "ч": "ch",
		"Џ": "Dzh", "џ": "dzh",
		"Ш": "Sh", "ш": "sh"
	}

	original_sys_stdin = None
	original_sys_stdout = None
	original_sys_stderr = None

	def __new__(cls):
		if not cls.courses:
			course_link_prefix = "http://courses.finki.ukim.mk/course/view.php?id="
			cls.courses = [
				CourseLink("MPS     Microprocessor Systems", f"{course_link_prefix}1335"),
				CourseLink("DB      Databases", f"{course_link_prefix}1345"),
				CourseLink("MIS     Management Information Systems", f"{course_link_prefix}1351"),
				CourseLink("MPIP    Mobile Platforms And Programming", f"{course_link_prefix}1331"),
				CourseLink("CN      Computer Networks", f"{course_link_prefix}1332"),
				CourseLink("PS      Probability And Statistics", f"{course_link_prefix}1306"),
				CourseLink("CN-MK   Computer Networks - MK", f"{course_link_prefix}1309")
			]


CommonVars()
