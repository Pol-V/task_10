from app import db

class GroupModel(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class StudentModel(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    group = db.relationship('GroupModel', backref=db.backref('students', lazy=True))

class CourseModel(db.Model):
    __tablename__ = 'courses'
    name = db.Column(db.String(255), primary_key=True)
    description = db.Column(db.String(255))





# class GroupModel:
# 	def __init__(self, name):
# 		self.name=name
#
# 	def set_list(self, lst=[], name):
# 		lst.append(name)




#
# class StudentModel:
# 	def __init__(self, group_id, first_name, last_name):
# 		self.group_id=group_id
# 		self.first_name=first_name
# 		self.last_name=last_name
#
# class CourseModel:
# 	def __init__(self, name, description):
# 		self.name=name
# 		self.description=description
#

