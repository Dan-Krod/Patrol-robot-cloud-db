from flask import Blueprint, request, jsonify
from auth.controller.sensor_controller import SensorController

sensor_blueprint = Blueprint('sensor', __name__)

@sensor_blueprint.route('/sensors', methods=['POST'])
def add_sensor():
    data = request.json
    response, status_code = SensorController.add_sensor(data)
    return jsonify(response), status_code

@sensor_blueprint.route('/sensors/<int:sensor_id>', methods=['GET'])
def get_sensor(sensor_id):
    response, status_code = SensorController.get_sensor(sensor_id)
    return jsonify(response), status_code

@sensor_blueprint.route('/sensors', methods=['GET'])
def get_all_sensors():
    response, status_code = SensorController.get_all_sensors()
    return jsonify(response), status_code

@sensor_blueprint.route('/sensors/<int:sensor_id>', methods=['PUT'])
def update_sensor(sensor_id):
    data = request.json
    response, status_code = SensorController.update_sensor(sensor_id, data)
    return jsonify(response), status_code

@sensor_blueprint.route('/sensors/<int:sensor_id>', methods=['DELETE'])
def delete_sensor(sensor_id):
    response, status_code = SensorController.delete_sensor(sensor_id)
    return jsonify(response), status_code

@sensor_blueprint.route('/sensors_with_robot', methods=['GET'])
def get_sensors_with_robot():
    response, status_code = SensorController.get_sensors_with_robot()
    return jsonify(response), status_code
