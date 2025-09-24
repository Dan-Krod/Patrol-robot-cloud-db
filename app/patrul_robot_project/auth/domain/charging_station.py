from auth.domain.models import db

class ChargingStation(db.Model):
    __tablename__ = 'charging_station'
    
    station_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(45), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Enum('yes', 'no'), nullable=False)
    
    robots = db.relationship('Robot', backref='charging_station', cascade='all, delete-orphan')
