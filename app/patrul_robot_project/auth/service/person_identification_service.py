from auth.dao.person_identification_dao import PersonIdentificationDAO

class PersonIdentificationService:
    @staticmethod
    def add_identification(person_name, timestamp, accuracy, sensor_id, camera_id, report_id):
        return PersonIdentificationDAO.add_identification(person_name, timestamp, accuracy, sensor_id, camera_id, report_id)

    @staticmethod
    def get_identification(identification_id):
        return PersonIdentificationDAO.get_identification(identification_id)

    @staticmethod
    def get_all_identifications():
        return PersonIdentificationDAO.get_all_identifications()

    @staticmethod
    def update_identification(identification_id, person_name, timestamp, accuracy, sensor_id, camera_id, report_id):
        return PersonIdentificationDAO.update_identification(identification_id, person_name, timestamp, accuracy, sensor_id, camera_id, report_id)

    @staticmethod
    def delete_identification(identification_id):
        return PersonIdentificationDAO.delete_identification(identification_id)
    
    @staticmethod
    def get_all_identifications_with_reports():
        return PersonIdentificationDAO.get_all_identifications_with_reports()
