# main_flask.py
# Alexander Wasserman
# 27 Feb 2025

from flask import Flask
from hmi.flask_app.routes import init_routes

def create_app():
    app = Flask(__name__)
    init_routes(app)  # Register routes from routes.py
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)  # or remove debug=True in production
