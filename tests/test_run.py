'''Created on 12.05.2017
@author: oggo'''

import pytest
from app import app


def test_get_all_books():
    response = app.test_client().get('/')
    assert b'Hello world Test app' in response.data

