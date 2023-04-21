import sqlalchemy


class GroupModel:
	def __init__(self, name):
		self.name=name


class StudentModel:
	def __init__(self, group_id, first_name, last_name):
		self.group_id=group_id
		self.first_name=first_name
		self.last_name=last_name

class CourseModel:
	def __init__(self, name, description):
		self.name=name
		self.description=description


