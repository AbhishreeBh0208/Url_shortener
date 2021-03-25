from Tool import db


class Urls(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    og_url = db.Column(db.String)
    short_url = db.Column(db.String)
