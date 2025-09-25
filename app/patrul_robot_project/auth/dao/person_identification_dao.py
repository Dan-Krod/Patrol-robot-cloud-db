from auth.domain.models import db
from auth.domain.person_identification import PersonIdentification

class PersonIdentificationDAO:
    @staticmethod
    def add_identification(person_name, timestamp, accuracy, sensor_id, camera_id, report_id):
        new_identification = PersonIdentification(person_name=person_name, timestamp=timestamp, accuracy=accuracy, sensor_id=sensor_id, camera_id=camera_id, report_id=report_id)
        db.session.add(new_identification)
        db.session.commit()
        return new_identification

    @staticmethod
    def get_identification(identification_id):
        return PersonIdentification.query.get(identification_id)

    @staticmethod
    def get_all_identifications():
        return PersonIdentification.query.all()

    @staticmethod
    def update_identification(identification_id, person_name, timestamp, accuracy, sensor_id, camera_id, report_id):
        identification = PersonIdentification.query.get(identification_id)
        if identification:
            identification.person_name = person_name
            identification.timestamp = timestamp
            identification.accuracy = accuracy
            identification.sensor_id = sensor_id
            identification.camera_id = camera_id
            identification.report_id = report_id
            db.session.commit()
        return identification

    @staticmethod
    def delete_identification(identification_id):
        identification = PersonIdentification.query.get(identification_id)
        if identification:
            db.session.delete(identification)
            db.session.commit()
        return identification

    @staticmethod
    def get_all_identifications_with_reports():
        return db.session.query(PersonIdentification).options(
            db.joinedload(PersonIdentification.report)
        ).all()