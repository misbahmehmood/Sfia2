from application import db
from application.models import Disney, Marvel

db.drop_all()
db.create_all()
