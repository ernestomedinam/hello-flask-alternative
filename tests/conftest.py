import pytest
import os
from flask import current_app, Flask
from app_name.app import create_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Engine, Connection, RootTransaction

# helper Resource class
class APIResource():
    def __init__(self, app_client, prefix):
        # init app client
        self.app_client = app_client
        self.prefix = prefix.strip("/")
        self.headers = { "Content-Type": "application/json" }

    def _delegate(self, method, path="", *args, **kwargs):
        # grab method fn
        app_client_fn = getattr(self.app_client, method)
        # prefix endpoint
        prefixed_path = os.path.join(self.prefix, path)
        # fetch
        return app_client_fn(prefixed_path, headers=self.headers, *args, **kwargs)

    def fetch(self, method="get", headers={}, *args, **kwargs):
        for (header, value) in headers.items():
            self.headers[header] = value
        return self._delegate(method, *args, **kwargs)

# declare fixture for app so tests get app with testing = True
@pytest.fixture(scope="session")
def app(request):
    app = create_app("test")
    app.testing = True
    with app.app_context():
        yield app

# fixture for pytest-flask-sqlalchemy
@pytest.fixture(scope="session")
def db(app, request):
    with app.app_context():
        from app_name.db import db, migrate
        db.init_app(app)
        migrate.init_app(app, db)
        return db

@pytest.fixture(scope="function")
def db_session(app: Flask, db: SQLAlchemy, request):
    """Creates a new database session for a test."""
    with app.app_context():
        engines = db.engines
    
    engine_cleanup = []
    for key, engine in engines.items():
        _engine: Engine = engine
        connection: Connection = _engine.connect()
        transaction: RootTransaction = connection.begin()
        engines[key] = connection
        engine_cleanup.append((key, _engine, connection, transaction))
    try:
        db.drop_all()
        db.create_all()
        yield db.session
    finally:
        for key, _engine, connection, transaction in engine_cleanup:
            transaction.rollback()
            db.session.remove()
            connection.close()
            engines[key] = engine

# fixture to use an api_client
@pytest.fixture(scope="function")
def client(app, db_session):
    with app.test_client() as _client:
        api_client = APIResource(_client, "api")
        yield api_client
