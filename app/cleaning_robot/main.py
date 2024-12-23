import connexion
from app.cleaning_robot.database import init_db


application_name = __name__


def create_app():
    connexion_app = connexion.App(application_name, specification_dir="../")
    connexion_app.add_api("openapi.v1.yml")
    return connexion_app


app = create_app()
init_db()


@app.route("/")
def root():
    return "<p>Welcome to Cleaning robot API</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
