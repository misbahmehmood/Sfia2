import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Cartoon
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                DEBUG=True
                )
        return app

    def setUp(self):
    
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()