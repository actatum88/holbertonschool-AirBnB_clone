#!/usr/bin/python3
"""File Storage Unittest"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage (unittest.TestCase):
    "unit test"
    def setUp(self):
        self.User1 = BaseModel()
        self.User2 = BaseModel()
        self.fsUser = FileStorage()
        storage.save()

    def tearDown(self):
        del self.User1
        del self.User2
        storage.save()

    def test_all(self):
        new_dict = self.fsUser.all()
        self.assertIsInstance(new_dict, dict)
        self.assertTrue(len(new_dict) > 0)