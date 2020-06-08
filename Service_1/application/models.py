from application import db

class Disney (db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    catchphrase=db.Column(db.String(50))

    def __repr__(self):
        return ''.join([
            'Name: ', self.name, '\r\n'
            'Catchphrase: ', self.catchphrase, '\r\n'
            ])

class Marvel (db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    catchphrase=db.Column(db.String(50))

    def __repr__(self):
        return ''.join([
            'Name: ', self.name, '\r\n'
            'Catchphrase: ', self.catchphrase, '\r\n'
            ])

