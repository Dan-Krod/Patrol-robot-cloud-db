from auth.domain.models import db

class Maintenance(db.Model):
    __tablename__ = 'maintenance'
    
    maintenance_id = db.Column(db.Integer, primary_key=True)
    maintenance_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)
    technician_name = db.Column(db.String(50), nullable=False)
    next_maintenance = db.Column(db.DateTime, nullable=False)

    robot_maintenances = db.relationship('RobotMaintenance', back_populates='maintenance')
    
    @property
    def robots(self):
        return [robot_maintenance.robot for robot_maintenance in self.robot_maintenances]