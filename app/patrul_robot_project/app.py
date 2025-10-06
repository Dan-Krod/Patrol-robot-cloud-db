from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from auth.domain.models import db
from auth.route.camera_route import camera_blueprint
from auth.route.charging_station_route import charging_station_blueprint
from auth.route.maintenance_route import maintenance_blueprint
from auth.route.operator_route import operator_blueprint
from auth.route.person_identification_route import person_identification_blueprint
from auth.route.robot_route import robot_blueprint
from auth.route.robot_maintenance_route import robot_maintenance_blueprint
from auth.route.sensor_route import sensor_blueprint
from auth.route.user_route import user_blueprint

load_dotenv()

app = Flask(__name__)

# Swagger config
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "My API",
        "description": "API for SCADA system",
        "version": "1.0"
    },
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
        }
    },
    "security": [{"BearerAuth": []}]
}

Swagger(app, config=swagger_config, template=swagger_template)

# DB config
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT config
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-key")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
jwt = JWTManager(app)

# Token blocklist
BLOCKLIST = set()

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    return jwt_payload["jti"] in BLOCKLIST

# Init DB
db.init_app(app)

# Register blueprints
app.register_blueprint(operator_blueprint)
app.register_blueprint(robot_blueprint)
app.register_blueprint(person_identification_blueprint)
app.register_blueprint(charging_station_blueprint)
app.register_blueprint(sensor_blueprint)
app.register_blueprint(camera_blueprint)
app.register_blueprint(maintenance_blueprint)
app.register_blueprint(robot_maintenance_blueprint)
app.register_blueprint(user_blueprint)

# Routes
@app.route('/')
def index():
    return "Підключення до бази даних успішне!"

@app.route('/api/health', methods=['GET'])
def health():
    """
    Health check
    ---
    responses:
      200:
        description: OK
        content:
          application/json:
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: ok
    """
    return {"status": "ok"}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
