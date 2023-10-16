#!/usr/bin/python3
'''initializing the Storage object'''

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
