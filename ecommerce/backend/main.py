# backend/main.py
from flask import Flask
from config import Config
from accounting_service.routes import accounting_bp
from product_service.routes import product_bp
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database connections
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(accounting_bp, url_prefix='/accounting')
    app.register_blueprint(product_bp, url_prefix='/products')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
