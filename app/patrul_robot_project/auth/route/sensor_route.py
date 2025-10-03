from flask import Blueprint, request, jsonify
from auth.controller.sensor_controller import SensorController

sensor_blueprint = Blueprint('sensor', __name__)

@sensor_blueprint.route('/sensors', methods=['POST'])
def add_sensor():
    """
    Add a new sensor
    ---
    tags:
      - Sensor
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - type
            - robot_id
          properties:
            type:
              type: string
              example: "Temperature"
            robot_id:
              type: integer
              example: 1
    responses:
      201:
        description: Sensor created successfully
      400:
        description: Invalid input
    """
    data = request.json
    response, status_code = SensorController.add_sensor(data)
    return jsonify(response), status_code


@sensor_blueprint.route('/sensors/<int:sensor_id>', methods=['GET'])
def get_sensor(sensor_id):
    """
    Get a sensor by ID
    ---
    tags:
      - Sensor
    parameters:
      - name: sensor_id
        in: path
        required: true
        type: integer
        description: ID of the sensor
    responses:
      200:
        description: Sensor data
      404:
        description: Sensor not found
    """
    response, status_code = SensorController.get_sensor(sensor_id)
    return jsonify(response), status_code


@sensor_blueprint.route('/sensors', methods=['GET'])
def get_all_sensors():
    """
    Get all sensors
    ---
    tags:
      - Sensor
    responses:
      200:
        description: List of all sensors
    """
    response, status_code = SensorController.get_all_sensors()
    return jsonify(response), status_code


@sensor_blueprint.route('/sensors/<int:sensor_id>', methods=['PUT'])
def update_sensor(sensor_id):
    """
    Update a sensor
    ---
    tags:
      - Sensor
    consumes:
      - application/json
    parameters:
      - name: sensor_id
        in: path
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            type:
              type: string
              example: "Humidity"
            robot_id:
              type: integer
              example: 2
    responses:
      200:
        description: Sensor updated successfully
      404:
        description: Sensor not found
    """
    data = request.json
    response, status_code = SensorController.update_sensor(sensor_id, data)
    return jsonify(response), status_code


@sensor_blueprint.route('/sensors/<int:sensor_id>', methods=['DELETE'])
def delete_sensor(sensor_id):
    """
    Delete a sensor
    ---
    tags:
      - Sensor
    parameters:
      - name: sensor_id
        in: path
        required: true
        type: integer
        description: ID of the sensor
    responses:
      200:
        description: Sensor deleted successfully
      404:
        description: Sensor not found
    """
    response, status_code = SensorController.delete_sensor(sensor_id)
    return jsonify(response), status_code


@sensor_blueprint.route('/sensors_with_robot', methods=['GET'])
def get_sensors_with_robot():
    """
    Get sensors along with their assigned robot
    ---
    tags:
      - Sensor
    responses:
      200:
        description: List of sensors with associated robot
    """
    response, status_code = SensorController.get_sensors_with_robot()
    return jsonify(response), status_code
