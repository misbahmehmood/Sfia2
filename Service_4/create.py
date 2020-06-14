from application import db
from application.models import Cartoon

db.drop_all()
db.create_all()
