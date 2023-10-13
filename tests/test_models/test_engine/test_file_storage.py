#!/usr/bin/python3
""" Define Tests for FileStorage"""

import unittest
from models.engine.file_storage import FileStorage


class TestFilestorage(unittest.TestCase):
    """this will the the class test for the Filestorage"""

    def test_all_method_returns_dict(self):
        """Function to test return of FileStorage"""
        storage = FileStorage()
        result = storage.all()
        self.assertIsInstance(result, dict)
