from application import db

class Disney(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(3000), nullable=False)

    def __repr__(self):
        return ''.join([
            'Name: ', self.name
            ])

class Marvel(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(3000), nullable=False)

    def __repr__(self):
        return ''.join([
            'Name: ', self.name
            ])

