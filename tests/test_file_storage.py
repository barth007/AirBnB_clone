#!/usr/bin/python3
"""Unit test file storage"""

import unittest
import pep8
from datetime import datetime
from models.engine.file_storage import Filestorage
from models import *


class  Test_FileStorage(unittest.TestCase):
    """ Test file storage"""

    def setup(self):
        self.store = FileStorage()

    def test_pep8_FileStorage(self):
        """Test pep8 style"""
        pep8style = pep8.styleGuide(quiet=True)
        p = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
    
    def test__attrs(self):
        """test for presence of attributes"""
        self.assertFalse(hasattr(self.store, "barthandkene.json"))
        
    def test_all(self):
        """ Test if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNOtNone(obj)
        self.assertEqual(typr(obj), dict)
        self.assertIs(obj, storage.FileStorage__objects)


if"__main__" == __name__:
    unittest.main()

