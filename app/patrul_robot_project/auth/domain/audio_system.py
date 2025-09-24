from auth.domain.models import db

class AudioSystem(db.Model):
    __tablename__ = 'audio_system'
    
    audio_system_id = db.Column(db.Integer, primary_key=True)
    has_speaker = db.Column(db.Enum('yes', 'no'), nullable=False)
    has_microphone = db.Column(db.Enum('yes', 'no'), nullable=False)
    has_panic_button = db.Column(db.Enum('yes', 'no'), nullable=False)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.robot_id'), nullable=False)
