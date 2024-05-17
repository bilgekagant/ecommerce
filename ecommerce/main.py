from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from accounting_service.models import db as accounting_db
from product_service.models import db as product_db
# from catalog_service.models import db as catalog_db
from accounting_service.routes import accounting_bp
from product_service.routes import product_bp
# from catalog_service.routes import catalog_bp
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    accounting_db.init_app(app)
    product_db.init_app(app)
    # catalog_db.init_app(app)
    # Import blueprints
    app.register_blueprint(accounting_bp, url_prefix='/accounting')
    app.register_blueprint(product_bp, url_prefix='/products')
    # app.register_blueprint(catalog_bp, url_prefix='/catalog')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
