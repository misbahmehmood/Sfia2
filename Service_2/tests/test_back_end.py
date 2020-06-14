import unittest
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        return app


class TestViews(TestBase):
    def test_access(self):
        response = self.client.get(url_for('names'))
        self.assertEqual(response.status_code, 200)