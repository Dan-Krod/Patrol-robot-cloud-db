from auth.service.person_identification_service import PersonIdentificationService

class PersonIdentificationController:

    @staticmethod
    def add_identification(data):
        required_fields = ['person_name', 'timestamp', 'accuracy', 'sensor_id', 'camera_id', 'report_id']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400

        identification = PersonIdentificationService.add_identification(
            person_name=data['person_name'],
            timestamp=data['timestamp'],
            accuracy=data['accuracy'],
            sensor_id=data['sensor_id'],
            camera_id=data['camera_id'],
            report_id=data['report_id']
        )
        return {'id': identification.identification_id}, 201

    @staticmethod
    def get_identification(identification_id):
        identification = PersonIdentificationService.get_identification(identification_id)
        if identification:
            return {
                'id': identification.identification_id,
                'person_name': identification.person_name,
                'timestamp': identification.timestamp,
                'accuracy': identification.accuracy,
                'sensor_id': identification.sensor_id,
                'camera_id': identification.camera_id,
                'report_id': identification.report_id
            }, 200
        return {'error': 'Person identification not found'}, 404

    @staticmethod
    def get_all_identifications():
        identifications = PersonIdentificationService.get_all_identifications()
        return [{
            'id': idf.identification_id,
            'person_name': idf.person_name,
            'timestamp': idf.timestamp,
            'accuracy': idf.accuracy,
            'sensor_id': idf.sensor_id,
            'camera_id': idf.camera_id,
            'report_id': idf.report_id
        } for idf in identifications], 200

    @staticmethod
    def update_identification(identification_id, data):
        required_fields = ['person_name', 'timestamp', 'accuracy', 'sensor_id', 'camera_id', 'report_id']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400

        identification = PersonIdentificationService.update_identification(
            identification_id,
            person_name=data['person_name'],
            timestamp=data['timestamp'],
            accuracy=data['accuracy'],
            sensor_id=data['sensor_id'],
            camera_id=data['camera_id'],
            report_id=data['report_id']
        )
        if identification:
            return {'message': 'Person identification updated'}, 200
        return {'error': 'Person identification not found'}, 404

    @staticmethod
    def delete_identification(identification_id):
        identification = PersonIdentificationService.delete_identification(identification_id)
        if identification:
            return {'message': 'Person identification deleted'}, 200
        return {'error': 'Person identification not found'}, 404

    @staticmethod
    def get_person_identifications_with_reports():
        identifications = PersonIdentificationService.get_all_identifications_with_reports()
        return [{
            'identification_id': ident.identification_id,
            'person_name': ident.person_name,
            'timestamp': ident.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'accuracy': str(ident.accuracy),
            'report': {
                'id': ident.report.report_id,
                'observations': ident.report.observations
            } if ident.report else None
        } for ident in identifications], 200
