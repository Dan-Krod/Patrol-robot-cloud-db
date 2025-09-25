from auth.domain.models import db
from auth.domain.charging_station import ChargingStation

class ChargingStationDAO:
    @staticmethod
    def add_station(location, capacity, available):
        new_station = ChargingStation(location=location, capacity=capacity, available=available)
        db.session.add(new_station)
        db.session.commit()
        return new_station

    @staticmethod
    def get_station(station_id):
        return ChargingStation.query.get(station_id)

    @staticmethod
    def get_all_stations():
        return ChargingStation.query.all()

    @staticmethod
    def update_station(station_id, location, capacity, available):
        station = ChargingStation.query.get(station_id)
        if station:
            station.location = location
            station.capacity = capacity
            station.available = available
            db.session.commit()
        return station

    @staticmethod
    def delete_station(station_id):
        station = ChargingStation.query.get(station_id)
        if station:
            db.session.delete(station)
            db.session.commit()
        return station

    @staticmethod
    def get_all_stations_with_robots():
        return ChargingStation.query.options(db.joinedload(ChargingStation.robots)).all()