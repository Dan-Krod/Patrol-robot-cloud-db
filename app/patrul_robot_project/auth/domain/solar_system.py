from auth.domain.models import db

class SolarSystem(db.Model):
    __tablename__ = 'solar_system'
    
    solar_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(45), nullable=False)
    power_output = db.Column(db.Float, nullable=False)
    technology_used = db.Column(db.String(45), nullable=False)
    station_id = db.Column(db.Integer, db.ForeignKey('charging_station.station_id'), nullable=False)
