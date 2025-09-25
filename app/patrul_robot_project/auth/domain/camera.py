from auth.domain.models import db

class Camera(db.Model):
    __tablename__ = 'camera'
    
    camera_id = db.Column(db.Integer, primary_key=True)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.robot_id'), nullable=False)
    resolution = db.Column(db.String(45), nullable=False)
    zoom_level = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    night_vision = db.Column(db.Enum('yes', 'no'), nullable=False)
    panoramic_view = db.Column(db.Enum('yes', 'no'), nullable=False)
