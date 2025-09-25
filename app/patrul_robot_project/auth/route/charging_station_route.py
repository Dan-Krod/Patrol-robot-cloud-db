from flask import Blueprint, request, jsonify
from auth.controller.charging_station_controller import ChargingStationController

charging_station_blueprint = Blueprint('charging_station', __name__)

@charging_station_blueprint.route('/charging_stations', methods=['POST'])
def add_station():
    data = request.json
    response, status_code = ChargingStationController.add_station(data)
    return jsonify(response), status_code

@charging_station_blueprint.route('/charging_stations/<int:station_id>', methods=['GET'])
def get_station(station_id):
    response, status_code = ChargingStationController.get_station(station_id)
    return jsonify(response), status_code

@charging_station_blueprint.route('/charging_stations', methods=['GET'])
def get_all_stations():
    response, status_code = ChargingStationController.get_all_stations()
    return jsonify(response), status_code

@charging_station_blueprint.route('/charging_stations/<int:station_id>', methods=['PUT'])
def update_station(station_id):
    data = request.json
    response, status_code = ChargingStationController.update_station(station_id, data)
    return jsonify(response), status_code

@charging_station_blueprint.route('/charging_stations/<int:station_id>', methods=['DELETE'])
def delete_station(station_id):
    response, status_code = ChargingStationController.delete_station(station_id)
    return jsonify(response), status_code

@charging_station_blueprint.route('/charging_stations_with_robots', methods=['GET'])
def get_charging_stations_with_robots():
    response, status_code = ChargingStationController.get_charging_stations_with_robots()
    return jsonify(response), status_code
