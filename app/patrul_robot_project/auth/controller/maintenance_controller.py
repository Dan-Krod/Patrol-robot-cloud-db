from auth.service.maintenance_service import MaintenanceService

class MaintenanceController:

    @staticmethod
    def add_maintenance(data):
        required_fields = ['maintenance_date', 'description', 'technician_name', 'next_maintenance']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400
        
        maintenance = MaintenanceService.add_maintenance(
            maintenance_date=data['maintenance_date'],
            description=data['description'],
            technician_name=data['technician_name'],
            next_maintenance=data['next_maintenance']
        )
        return {'id': maintenance.maintenance_id}, 201

    @staticmethod
    def get_maintenance(maintenance_id):
        maintenance = MaintenanceService.get_maintenance(maintenance_id)
        if maintenance:
            return {
                'id': maintenance.maintenance_id,
                'maintenance_date': maintenance.maintenance_date.strftime('%Y-%m-%d %H:%M:%S'),
                'description': maintenance.description,
                'technician_name': maintenance.technician_name,
                'next_maintenance': maintenance.next_maintenance.strftime('%Y-%m-%d %H:%M:%S')
            }, 200
        return {'error': 'Maintenance not found'}, 404

    @staticmethod
    def get_all_maintenances():
        maintenances = MaintenanceService.get_all_maintenances()
        return [{
            'id': maintenance.maintenance_id,
            'maintenance_date': maintenance.maintenance_date.strftime('%Y-%m-%d %H:%M:%S'),
            'description': maintenance.description,
            'technician_name': maintenance.technician_name,
            'next_maintenance': maintenance.next_maintenance.strftime('%Y-%m-%d %H:%M:%S')
        } for maintenance in maintenances], 200

    @staticmethod
    def update_maintenance(maintenance_id, data):
        required_fields = ['maintenance_date', 'description', 'technician_name', 'next_maintenance']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400

        maintenance = MaintenanceService.update_maintenance(
            maintenance_id,
            maintenance_date=data['maintenance_date'],
            description=data['description'],
            technician_name=data['technician_name'],
            next_maintenance=data['next_maintenance']
        )
        if maintenance:
            return {'message': 'Maintenance updated'}, 200
        return {'error': 'Maintenance not found'}, 404

    @staticmethod
    def delete_maintenance(maintenance_id):
        maintenance = MaintenanceService.delete_maintenance(maintenance_id)
        if maintenance:
            return {'message': 'Maintenance deleted'}, 200
        return {'error': 'Maintenance not found'}, 404
