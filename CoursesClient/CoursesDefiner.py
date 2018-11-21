from Common.CommonVars import CommonVars
from CoursesModels.Links.CourseLink import CourseLink


def define_current_courses():
	CommonVars.courses = [
		CourseLink("MPS     Microprocessor Systems", "http://courses.finki.ukim.mk/course/view.php?id=1335"),
		CourseLink("DB      Databases", "http://courses.finki.ukim.mk/course/view.php?id=1345"),
		CourseLink("MIS     Management Information Systems", "http://courses.finki.ukim.mk/course/view.php?id=1351"),
		CourseLink("MPIP    Mobile Platforms And Programming", "http://courses.finki.ukim.mk/course/view.php?id=1331"),
		CourseLink("CN      Computer Networks", "http://courses.finki.ukim.mk/course/view.php?id=1332"),
		CourseLink("PS      Probability And Statistics", "http://courses.finki.ukim.mk/course/view.php?id=1306"),
		CourseLink("CN-MK   Computer Networks - MK", "http://courses.finki.ukim.mk/course/view.php?id=1309")
	]
