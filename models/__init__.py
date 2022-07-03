#!/usr/bin/python3
"""
    The __init__.py file is used to perform import configurations.
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
