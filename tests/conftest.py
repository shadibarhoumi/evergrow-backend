import os

import pytest
from evergrowpdf import create_app

@pytest.fixture
def app():
    app = create_app({
        'ENV': 'development',
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
