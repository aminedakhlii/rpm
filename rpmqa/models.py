from rpmqa import db

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)