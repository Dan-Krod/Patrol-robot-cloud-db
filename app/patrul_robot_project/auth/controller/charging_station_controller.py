from auth.service.charging_station_service import ChargingStationService

class ChargingStationController:

    @staticmethod
    def add_station(data):
        required_fields = ['location', 'capacity', 'available']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400
        
        station = ChargingStationService.add_station(
            location=data['location'],
            capacity=data['capacity'],
            available=data['available']
        )
        return {'id': station.station_id}, 201

    @staticmethod
    def get_station(station_id):
        station = ChargingStationService.get_station(station_id)
        if station:
            return {
                'id': station.station_id,
                'location': station.location,
                'capacity': station.capacity,
                'available': station.available
            }, 200
        return {'error': 'Charging station not found'}, 404

    @staticmethod
    def get_all_stations():
        stations = ChargingStationService.get_all_stations()
        return [{
            'id': st.station_id,
            'location': st.location,
            'capacity': st.capacity,
            'available': st.available
        } for st in stations], 200

    @staticmethod
    def update_station(station_id, data):
        required_fields = ['location', 'capacity', 'available']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400
        
        station = ChargingStationService.update_station(
            station_id,
            location=data['location'],
            capacity=data['capacity'],
            available=data['available']
        )
        if station:
            return {'message': 'Charging station updated'}, 200
        return {'error': 'Charging station not found'}, 404

    @staticmethod
    def delete_station(station_id):
        station = ChargingStationService.delete_station(station_id)
        if station:
            return {'message': 'Charging station deleted'}, 200
        return {'error': 'Charging station not found'}, 404

    @staticmethod
    def get_charging_stations_with_robots():
        stations = ChargingStationService.get_all_stations_with_robots()
        return [{
            'id': st.station_id,
            'location': st.location,
            'capacity': st.capacity,
            'available': st.available,
            'robots': [{
                'id': rb.robot_id,
                'status': rb.status,
                'max_distance': rb.max_distance,
                'alternative_power_source': rb.alternative_power_source
            } for rb in st.robots]
        } for st in stations], 200
