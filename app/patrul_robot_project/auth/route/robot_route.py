from flask import Blueprint, request, jsonify
from auth.controller.robot_controller import RobotController

robot_blueprint = Blueprint('robot', __name__)

@robot_blueprint.route('/robots', methods=['POST'])
def add_robot():
    data = request.json
    response, status_code = RobotController.add_robot(data)
    return jsonify(response), status_code

@robot_blueprint.route('/robots/<int:robot_id>', methods=['GET'])
def get_robot(robot_id):
    response, status_code = RobotController.get_robot(robot_id)
    return jsonify(response), status_code

@robot_blueprint.route('/robots', methods=['GET'])
def get_all_robots():
    response, status_code = RobotController.get_all_robots()
    return jsonify(response), status_code

@robot_blueprint.route('/robots/<int:robot_id>', methods=['PUT'])
def update_robot(robot_id):
    data = request.json
    response, status_code = RobotController.update_robot(robot_id, data)
    return jsonify(response), status_code

@robot_blueprint.route('/robots/<int:robot_id>', methods=['DELETE'])
def delete_robot(robot_id):
    response, status_code = RobotController.delete_robot(robot_id)
    return jsonify(response), status_code
