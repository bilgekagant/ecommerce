from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Import blueprints
    from accounting_service.routes import accounting_bp
    app.register_blueprint(accounting_bp, url_prefix='/accounting')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
