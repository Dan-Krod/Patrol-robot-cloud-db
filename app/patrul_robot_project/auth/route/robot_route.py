from flask import Blueprint, request, jsonify
from auth.controller.robot_controller import RobotController

robot_blueprint = Blueprint('robot', __name__)


@robot_blueprint.route('/robots', methods=['POST'])
def add_robot():
    """
    Add a new robot
    ---
    tags:
      - Robot
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - status
            - max_distance
            - operator_id
            - station_id
            - alternative_power_source
          properties:
            status:
              type: string
              example: active
            max_distance:
              type: integer
              example: 150
            operator_id:
              type: integer
              example: 1
            station_id:
              type: integer
              example: 2
            alternative_power_source:
              type: string
              enum: [yes, no]
              example: yes
    responses:
      201:
        description: Robot created successfully
      400:
        description: Invalid input
    """
    data = request.json
    response, status_code = RobotController.add_robot(data)
    return jsonify(response), status_code


@robot_blueprint.route('/robots/<int:robot_id>', methods=['GET'])
def get_robot(robot_id):
    """
    Get a robot by ID
    ---
    tags:
      - Robot
    parameters:
      - name: robot_id
        in: path
        type: integer
        required: true
        description: ID of the robot
    responses:
      200:
        description: Robot data
      404:
        description: Robot not found
    """
    response, status_code = RobotController.get_robot(robot_id)
    return jsonify(response), status_code


@robot_blueprint.route('/robots', methods=['GET'])
def get_all_robots():
    """
    Get all robots
    ---
    tags:
      - Robot
    responses:
      200:
        description: List of robots
    """
    response, status_code = RobotController.get_all_robots()
    return jsonify(response), status_code


@robot_blueprint.route('/robots/<int:robot_id>', methods=['PUT'])
def update_robot(robot_id):
    """
    Update a robot
    ---
    tags:
      - Robot
    consumes:
      - application/json
    parameters:
      - name: robot_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            status:
              type: string
              example: inactive
            max_distance:
              type: integer
              example: 120
            operator_id:
              type: integer
              example: 1
            station_id:
              type: integer
              example: 2
            alternative_power_source:
              type: string
              enum: [yes, no]
              example: no
    responses:
      200:
        description: Robot updated successfully
      404:
        description: Robot not found
    """
    data = request.json
    response, status_code = RobotController.update_robot(robot_id, data)
    return jsonify(response), status_code


@robot_blueprint.route('/robots/<int:robot_id>', methods=['DELETE'])
def delete_robot(robot_id):
    """
    Delete a robot
    ---
    tags:
      - Robot
    parameters:
      - name: robot_id
        in: path
        type: integer
        required: true
        description: ID of the robot
    responses:
      200:
        description: Robot deleted successfully
      404:
        description: Robot not found
    """
    response, status_code = RobotController.delete_robot(robot_id)
    return jsonify(response), status_code
