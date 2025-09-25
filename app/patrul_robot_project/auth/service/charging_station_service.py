from auth.dao.charging_station_dao import ChargingStationDAO

class ChargingStationService:
    @staticmethod
    def add_station(location, capacity, available):
        return ChargingStationDAO.add_station(location, capacity, available)

    @staticmethod
    def get_station(station_id):
        return ChargingStationDAO.get_station(station_id)

    @staticmethod
    def get_all_stations():
        return ChargingStationDAO.get_all_stations()

    @staticmethod
    def update_station(station_id, location, capacity, available):
        return ChargingStationDAO.update_station(station_id, location, capacity, available)

    @staticmethod
    def delete_station(station_id):
        return ChargingStationDAO.delete_station(station_id)

    @staticmethod
    def get_all_stations_with_robots():
        return ChargingStationDAO.get_all_stations_with_robots()
