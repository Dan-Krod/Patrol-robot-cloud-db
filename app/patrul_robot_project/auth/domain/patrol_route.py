from auth.domain.models import db

class PatrolRoute(db.Model):
    __tablename__ = 'patrol_route'
    
    routes_id = db.Column(db.Integer, primary_key=True)
    start_point = db.Column(db.String(100), nullable=False)
    end_point = db.Column(db.String(100), nullable=False)
    difficulty_level = db.Column(db.Float, nullable=False)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.robot_id'), nullable=False)
