from auth.domain.models import db
from auth.domain.solar_system import SolarSystem

class SolarSystemDAO:
    @staticmethod
    def add_solar_system(status, power_output, technology_used, station_id):
        new_solar_system = SolarSystem(status=status, power_output=power_output, technology_used=technology_used, station_id=station_id)
        db.session.add(new_solar_system)
        db.session.commit()
        return new_solar_system

    @staticmethod
    def get_solar_system(solar_id):
        return SolarSystem.query.get(solar_id)

    @staticmethod
    def get_all_solar_systems():
        return SolarSystem.query.all()

    @staticmethod
    def update_solar_system(solar_id, status, power_output, technology_used, station_id):
        solar_system = SolarSystem.query.get(solar_id)
        if solar_system:
            solar_system.status = status
            solar_system.power_output = power_output
            solar_system.technology_used = technology_used
            solar_system.station_id = station_id
            db.session.commit()
        return solar_system

    @staticmethod
    def delete_solar_system(solar_id):
        solar_system = SolarSystem.query.get(solar_id)
        if solar_system:
            db.session.delete(solar_system)
            db.session.commit()
        return solar_system
