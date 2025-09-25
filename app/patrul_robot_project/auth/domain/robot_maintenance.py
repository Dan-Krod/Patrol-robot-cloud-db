from sqlalchemy import Column, Integer, ForeignKey
from auth.domain.models import db

class RobotMaintenance(db.Model):
    __tablename__ = 'robot_maintenance'

    robot_id = Column(Integer, ForeignKey('robot.robot_id'), primary_key=True)
    maintenance_id = Column(Integer, ForeignKey('maintenance.maintenance_id'), primary_key=True)

    robot = db.relationship('Robot', back_populates='maintenances')
    maintenance = db.relationship('Maintenance', back_populates='robot_maintenances')
