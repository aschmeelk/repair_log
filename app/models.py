from app import db


class Repairs(db.Model):
	"""docstring for Repairs"""
	id = db.Column(db.Integer, primary_key = True)
	date = db.Column(db.Date)
	pc_num = db.Column(db.Integer)
	franchise = db.Column(db.String(64))
	problem = db.Column(db.String(128))
	solution = db.Column(db.String(128))
	tech = db.Column(db.String(64))
	pc_app = db.Column(db.String(64))
	pc_mb = db.Column(db.String(64))

	def __repr__(self):
		return '<Repairs %r>' % (self.pc_num)