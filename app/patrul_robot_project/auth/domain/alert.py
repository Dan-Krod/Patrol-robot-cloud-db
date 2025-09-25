from auth.domain.models import db

class Alert(db.Model):
    __tablename__ = 'alert'
    
    alerts_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    audio_system_id = db.Column(db.Integer, db.ForeignKey('audio_system.audio_system_id'), nullable=False)
