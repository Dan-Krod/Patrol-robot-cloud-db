from flask import Blueprint, request, jsonify
from auth.controller.charging_station_controller import ChargingStationController

charging_station_blueprint = Blueprint('charging_station', __name__)


@charging_station_blueprint.route('/charging_stations', methods=['POST'])
def add_station():
    """
    Add a new charging station
    ---
    tags:
      - Charging Station
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - location
            - capacity
          properties:
            location:
              type: string
              example: "Sector A - Dock 3"
            capacity:
              type: integer
              example: 4
    responses:
      201:
        description: Charging station created successfully
      400:
        description: Invalid input
    """
    data = request.json
    response, status_code = ChargingStationController.add_station(data)
    return jsonify(response), status_code


@charging_station_blueprint.route('/charging_stations/<int:station_id>', methods=['GET'])
def get_station(station_id):
    """
    Get a charging station by ID
    ---
    tags:
      - Charging Station
    parameters:
      - name: station_id
        in: path
        required: true
        type: integer
        description: ID of the charging station
    responses:
      200:
        description: Charging station data
      404:
        description: Charging station not found
    """
    response, status_code = ChargingStationController.get_station(station_id)
    return jsonify(response), status_code


@charging_station_blueprint.route('/charging_stations', methods=['GET'])
def get_all_stations():
    """
    Get all charging stations
    ---
    tags:
      - Charging Station
    responses:
      200:
        description: List of all charging stations
    """
    response, status_code = ChargingStationController.get_all_stations()
    return jsonify(response), status_code


@charging_station_blueprint.route('/charging_stations/<int:station_id>', methods=['PUT'])
def update_station(station_id):
    """
    Update a charging station
    ---
    tags:
      - Charging Station
    consumes:
      - application/json
    parameters:
      - name: station_id
        in: path
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            location:
              type: string
              example: "Sector B - Dock 1"
            capacity:
              type: integer
              example: 6
    responses:
      200:
        description: Charging station updated successfully
      404:
        description: Charging station not found
    """
    data = request.json
    response, status_code = ChargingStationController.update_station(station_id, data)
    return jsonify(response), status_code


@charging_station_blueprint.route('/charging_stations/<int:station_id>', methods=['DELETE'])
def delete_station(station_id):
    """
    Delete a charging station
    ---
    tags:
      - Charging Station
    parameters:
      - name: station_id
        in: path
        required: true
        type: integer
        description: ID of the charging station
    responses:
      200:
        description: Charging station deleted successfully
      404:
        description: Charging station not found
    """
    response, status_code = ChargingStationController.delete_station(station_id)
    return jsonify(response), status_code


@charging_station_blueprint.route('/charging_stations_with_robots', methods=['GET'])
def get_charging_stations_with_robots():
    """
    Get charging stations with assigned robots
    ---
    tags:
      - Charging Station
    responses:
      200:
        description: List of charging stations and their robots
    """
    response, status_code = ChargingStationController.get_charging_stations_with_robots()
    return jsonify(response), status_code
