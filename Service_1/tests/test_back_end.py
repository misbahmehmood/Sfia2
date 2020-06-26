import unittest
from flask import url_for 
from flask_testing import TestCase
from application import app, db, routes
from application.models import Cartoon
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            SQLACADEMY_DATABASE_URI = getenv('PROJECT_URI'),
            DEBUG = True
        )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestModels(TestBase):
    def test_repr(self):
        character = Cartoon(name = 'Winnie the Pooh',
        information= 'Bear',
        profiletype= 'Species')
        print(repr(character))
