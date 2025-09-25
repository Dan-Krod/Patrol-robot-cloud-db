from auth.domain.models import db

class Operator(db.Model):
    __tablename__ = 'operator'
    
    operators_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    shift_start = db.Column(db.Time, nullable=False)
    shift_end = db.Column(db.Time, nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    
    robots = db.relationship('Robot', backref='operator', cascade='all, delete-orphan')
