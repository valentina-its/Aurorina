from app import db

class User(db.Model):
    __tablename__ = 'users'
    
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(120), nullable=False)