from auth.domain.models import db

class Sensor(db.Model):
    __tablename__ = 'sensor'
    
    sensor_id = db.Column(db.Integer, primary_key=True)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.robot_id'), nullable=False)
    technology_used = db.Column(db.String(50), nullable=False)
    detection_range = db.Column(db.Integer, nullable=False)
    trigger_status = db.Column(db.String(45), nullable=False)

