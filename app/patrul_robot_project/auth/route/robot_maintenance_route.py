from flask import Blueprint, request, jsonify
from auth.controller.robot_maintenance_controller import RobotMaintenanceController

robot_maintenance_blueprint = Blueprint('robot_maintenance', __name__)

@robot_maintenance_blueprint.route('/maintenances/<int:robot_id>', methods=['GET'])
def get_maintenances_for_robot(robot_id):
    """
    Get all maintenance records for a specific robot
    ---
    tags:
      - Robot Maintenance
    parameters:
      - name: robot_id
        in: path
        required: true
        type: integer
        description: ID of the robot
    responses:
      200:
        description: List of maintenance records for the robot
      404:
        description: Robot not found
    """
    response, status_code = RobotMaintenanceController.get_maintenances_for_robot(robot_id)
    return jsonify(response), status_code


@robot_maintenance_blueprint.route('/maintenances_with_robots', methods=['GET'])
def get_all_maintenances_with_robots():
    """
    Get all maintenance records along with their associated robots
    ---
    tags:
      - Robot Maintenance
    responses:
      200:
        description: List of maintenance records with related robots
    """
    response, status_code = RobotMaintenanceController.get_all_maintenances_with_robots()
    return jsonify(response), status_code


@robot_maintenance_blueprint.route('/robot_maintenance/<int:maintenance_id>', methods=['GET'])
def get_maintenance_with_robots(maintenance_id):
    """
    Get a specific maintenance record along with associated robot information
    ---
    tags:
      - Robot Maintenance
    parameters:
      - name: maintenance_id
        in: path
        required: true
        type: integer
        description: ID of the maintenance record
    responses:
      200:
        description: Maintenance record with associated robot
      404:
        description: Maintenance record not found
    """
    response, status_code = RobotMaintenanceController.get_maintenance_with_robots(maintenance_id)
    return jsonify(response), status_code
