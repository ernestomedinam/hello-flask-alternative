import pytest
from app_name.app import create_app

def test_dev_config():
    """ tests config variables for development """
    app = create_app()
    assert app.config["ENV"] == "development"
    assert app.config["DEBUG"] == True

def test_test_config(app):
    """ tests config variables for test """
    assert app.config["TESTING"] == True
    assert app.config["ENV"] == "development"
    assert app.config["DEBUG"] == True
