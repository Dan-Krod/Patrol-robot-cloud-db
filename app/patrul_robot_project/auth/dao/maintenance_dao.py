from auth.domain.models import db
from auth.domain.maintance import Maintenance

class MaintenanceDAO:
    @staticmethod
    def add_maintenance(maintenance_date, description, technician_name, next_maintenance):
        new_maintenance = Maintenance(maintenance_date=maintenance_date, description=description, technician_name=technician_name, next_maintenance=next_maintenance)
        db.session.add(new_maintenance)
        db.session.commit()
        return new_maintenance

    @staticmethod
    def get_maintenance(maintenance_id):
        return Maintenance.query.get(maintenance_id)
    
    @staticmethod
    def get_all_maintenances():
        return Maintenance.query.all()

    @staticmethod
    def update_maintenance(maintenance_id, maintenance_date, description, technician_name, next_maintenance):
        maintenance = Maintenance.query.get(maintenance_id)
        if maintenance:
            maintenance.maintenance_date = maintenance_date
            maintenance.description = description
            maintenance.technician_name = technician_name
            maintenance.next_maintenance = next_maintenance
            db.session.commit()
        return maintenance

    @staticmethod
    def delete_maintenance(maintenance_id):
        maintenance = Maintenance.query.get(maintenance_id)
        if maintenance:
            db.session.delete(maintenance)
            db.session.commit()
        return maintenance