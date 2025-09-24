from auth.domain.models import db

class Battery(db.Model):
    __tablename__ = 'battery'
    
    battery_id = db.Column(db.Integer, primary_key=True)
    log_time = db.Column(db.DateTime, nullable=False)
    battery_level = db.Column(db.Integer, nullable=False)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.robot_id'), nullable=False)
    temperature = db.Column(db.String(45), nullable=False)

