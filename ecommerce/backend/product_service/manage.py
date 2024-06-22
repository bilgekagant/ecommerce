# backend/product_service/manage.py
import sys
from flask import Flask
from flask_migrate import Migrate
sys.path.append('..')  # This allows us to import config from the parent directory
from config import Config
from extensions import db
from models import Product

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        from flask_migrate import upgrade, migrate, revision, init, branches, heads
        if len(sys.argv) > 1 and sys.argv[1] == 'db':
            if len(sys.argv) > 2:
                if sys.argv[2] == 'init':
                    init()
                elif sys.argv[2] == 'migrate':
                    migrate()
                elif sys.argv[2] == 'upgrade':
                    upgrade()
                elif sys.argv[2] == 'revision':
                    revision()
                elif sys.argv[2] == 'branches':
                    branches()
                elif sys.argv[2] == 'heads':
                    heads()
            else:
                print("Usage: python manage.py db <command>")
                print("Commands: init, migrate, upgrade")
        else:
            app.run(debug=True)
