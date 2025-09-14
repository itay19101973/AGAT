from flask import Flask
from .config import SQL_ALCHEMY_DB_CONNECTION_URL, BACKEND_SERVER_PORT
from .routes.ai import ai_bp
from .database import get_db_connection


def setup_app():
    app = Flask(__name__)

    # for postgres db
    app.config['SQLALCHEMY_DATABASE_URI'] = SQL_ALCHEMY_DB_CONNECTION_URL
    db = get_db_connection()
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # routes
    app.register_blueprint(ai_bp)

    return app


application = setup_app()

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=BACKEND_SERVER_PORT, debug=True)
