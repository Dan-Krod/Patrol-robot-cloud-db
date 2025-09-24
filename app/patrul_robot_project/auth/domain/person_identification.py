from auth.domain.models import db

class PersonIdentification(db.Model):
    __tablename__ = 'person_identification'
    
    identification_id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    accuracy = db.Column(db.Numeric(5, 2), nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.sensor_id'), nullable=False)
    camera_id = db.Column(db.Integer, db.ForeignKey('camera.camera_id'), nullable=False)
    report_id = db.Column(db.Integer, db.ForeignKey('patrol_report.report_id'), nullable=False)
    
    report = db.relationship('PatrolReport', backref='person_identifications')
