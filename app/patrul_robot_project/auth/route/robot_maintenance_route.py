from flask import Blueprint, request, jsonify
from auth.controller.robot_maintenance_controller import RobotMaintenanceController

robot_maintenance_blueprint = Blueprint('robot_maintenance', __name__)

@robot_maintenance_blueprint.route('/maintenances/<int:robot_id>', methods=['GET'])
def get_maintenances_for_robot(robot_id):
    response, status_code = RobotMaintenanceController.get_maintenances_for_robot(robot_id)
    return jsonify(response), status_code

@robot_maintenance_blueprint.route('/maintenances_with_robots', methods=['GET'])
def get_all_maintenances_with_robots():
    response, status_code = RobotMaintenanceController.get_all_maintenances_with_robots()
    return jsonify(response), status_code

@robot_maintenance_blueprint.route('/robot_maintenance/<int:maintenance_id>', methods=['GET'])
def get_maintenance_with_robots(maintenance_id):
    response, status_code = RobotMaintenanceController.get_maintenance_with_robots(maintenance_id)
    return jsonify(response), status_code
