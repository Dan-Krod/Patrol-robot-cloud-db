from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(operator_blueprint)  
app.register_blueprint(robot_blueprint) 
app.register_blueprint(person_identification_blueprint) 
app.register_blueprint(charging_station_blueprint) 
app.register_blueprint(sensor_blueprint) 
app.register_blueprint(camera_blueprint)
app.register_blueprint(maintenance_blueprint)
app.register_blueprint(robot_maintenance_blueprint)

@app.route('/')
def index():
    return "Підключення до бази даних успішне!"

if __name__ == '__main__':
    app.run(debug=True)
