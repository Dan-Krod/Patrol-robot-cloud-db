from flask_sqlalchemy import SQLAlchemy

# Ініціалізація SQLAlchemy
db = SQLAlchemy()

# Імпорт усіх моделей
from .operator import Operator
from .charging_station import ChargingStation
from .robot import Robot
from .audio_system import AudioSystem
from .alert import Alert
from .battery import Battery
from .camera import Camera
from .maintance import Maintenance
from .patrol_route import PatrolRoute
from .patrol_report import PatrolReport
from .sensor import Sensor
from .person_identification import PersonIdentification
from .solar_system import SolarSystem
from .robot_maintenance import RobotMaintenance