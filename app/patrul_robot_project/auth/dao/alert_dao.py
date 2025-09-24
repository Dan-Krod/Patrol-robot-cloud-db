from auth.domain.models import db
from auth.domain.alert import Alert

class AlertDAO:
    @staticmethod
    def add_alert(alert_type, timestamp, status, audio_system_id):
        new_alert = Alert(type=alert_type, timestamp=timestamp, status=status, audio_system_id=audio_system_id)
        db.session.add(new_alert)
        db.session.commit()
        return new_alert

    @staticmethod
    def get_alert(alerts_id):
        return Alert.query.get(alerts_id)

    @staticmethod
    def get_all_alerts():
        return Alert.query.all()

    @staticmethod
    def update_alert(alerts_id, alert_type, timestamp, status, audio_system_id):
        alert = Alert.query.get(alerts_id)
        if alert:
            alert.type = alert_type
            alert.timestamp = timestamp
            alert.status = status
            alert.audio_system_id = audio_system_id
            db.session.commit()
        return alert

    @staticmethod
    def delete_alert(alerts_id):
        alert = Alert.query.get(alerts_id)
        if alert:
            db.session.delete(alert)
            db.session.commit()
        return alert
