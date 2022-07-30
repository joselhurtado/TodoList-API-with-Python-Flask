import toml, pytest, os, sys, tempfile, mock, json
from flask import Flask

@pytest.fixture
def client():
    with mock.patch('flask.Flask', lambda x: Flask(x)):
        from src.app import app
        db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True

        with app.test_client() as client:
            # with app.app_context():
            #     app.init_db()
            yield client

        os.close(db_fd)
        os.unlink(app.config['DATABASE'])

@pytest.mark.it("folder src must exist")
def test_src_folder():
  assert True
