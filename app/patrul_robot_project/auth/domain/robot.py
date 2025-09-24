from auth.domain.models import db

class Robot(db.Model):
    __tablename__ = 'robot'
    
    robot_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    max_distance = db.Column(db.Integer, nullable=False)
    operator_id = db.Column(db.Integer, db.ForeignKey('operator.operators_id'), nullable=False)
    station_id = db.Column(db.Integer, db.ForeignKey('charging_station.station_id'), nullable=False)
    alternative_power_source = db.Column(db.Enum('yes', 'no'), nullable=False)

    audio_systems = db.relationship('AudioSystem', backref='robot', cascade='all, delete-orphan')
    batteries = db.relationship('Battery', backref='robot', cascade='all, delete-orphan')
    cameras = db.relationship('Camera', backref='robot', cascade='all, delete-orphan')
    maintenances = db.relationship('RobotMaintenance', back_populates='robot', lazy='dynamic')
    patrol_routes = db.relationship('PatrolRoute', backref='robot', cascade='all, delete-orphan')
    sensors = db.relationship('Sensor', backref='robot', cascade='all, delete-orphan')