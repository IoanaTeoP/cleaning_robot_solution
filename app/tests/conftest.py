from app.cleaning_robot.main import create_app
from app.cleaning_robot.database import session_context
from app.cleaning_robot.path_calculation.models import PathCalculationExecution
from app.tests.fixtures import *  # noqa


@pytest.fixture()
def flask_test_app():
    connexion_app = create_app()
    yield connexion_app


@pytest.fixture()
def client(flask_test_app):
    return flask_test_app.test_client()


@pytest.fixture(autouse=True, scope="function")
def cleanup_db():
    with session_context() as session:
        session.query(PathCalculationExecution).delete()
        session.commit()


@pytest.fixture
def db_session():
    with session_context() as session:
        session.expire_on_commit = False
    yield session
