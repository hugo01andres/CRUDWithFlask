from app import db

class Contact(db.Model):
    id : int = db.Column(db.Integer, primary_key=True)
    name : str = db.Column(db.String(100), nullable=False)
    email : str = db.Column(db.String(100), nullable=False)
    phone : str = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
