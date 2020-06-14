from application import db

class Cartoon(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    information=db.Column(db.String(50), nullable=False)
    profiletype=db.Column(db.String(20), nullable=False)



    def __repr__(self):
        return ''.join([
            'Name: ', self.name, '\r\n',
            'Information: ', self.information, '\r\n'
            'Type: ', self.profiletype
            ])

