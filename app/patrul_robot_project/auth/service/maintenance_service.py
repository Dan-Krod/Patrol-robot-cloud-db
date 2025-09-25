from auth.dao.maintenance_dao import MaintenanceDAO

class MaintenanceService:
    @staticmethod
    def add_maintenance(maintenance_date, description, technician_name, next_maintenance):
        return MaintenanceDAO.add_maintenance(maintenance_date, description, technician_name, next_maintenance)

    @staticmethod
    def get_maintenance(maintenance_id):
        return MaintenanceDAO.get_maintenance(maintenance_id)

    @staticmethod
    def get_all_maintenances():
        return MaintenanceDAO.get_all_maintenances()

    @staticmethod
    def update_maintenance(maintenance_id, maintenance_date, description, technician_name, next_maintenance):
        return MaintenanceDAO.update_maintenance(maintenance_id, maintenance_date, description, technician_name, next_maintenance)

    @staticmethod
    def delete_maintenance(maintenance_id):
        return MaintenanceDAO.delete_maintenance(maintenance_id)
