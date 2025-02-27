# main_flask.py
# Alexander Wasserman
# 27 Feb 2025

from flask import Flask
from hmi.flask_app.routes import init_routes

def create_app():
    app = Flask(__name__, template_folder="hmi/templates", static_folder="hmi/static")
    init_routes(app)  # Register routes from routes.py
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=False)
