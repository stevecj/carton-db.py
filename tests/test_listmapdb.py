import os
from os import path
from os.path import realpath, dirname

import pytest

import cartondb as cdb

project_root = dirname(dirname(realpath(__file__)))

@pytest.fixture
def subject():
    return cdb.ListMapDB(full_db_name)

@pytest.fixture
def workspace_dir():
    ws_dir = path.join(project_root, 'tmp', 'test_listmapdb')
    if path.isdir(ws_dir):
        os.removedirs(ws_dir)
    os.makedirs(ws_dir)
    return ws_dir

@pytest.fixture
def full_db_name(workspace_dir):
    return path.join(workspace_dir, 'the_database')

def test_something(full_db_name):
    pass
