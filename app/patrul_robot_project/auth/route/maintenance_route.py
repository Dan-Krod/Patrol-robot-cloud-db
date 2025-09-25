from flask import Blueprint, request, jsonify
from auth.controller.maintenance_controller import MaintenanceController

maintenance_blueprint = Blueprint('maintenance', __name__)

@maintenance_blueprint.route('/maintenances', methods=['POST'])
def add_maintenance():
    data = request.json
    response, status_code = MaintenanceController.add_maintenance(data)
    return jsonify(response), status_code

@maintenance_blueprint.route('/maintenances/<int:maintenance_id>', methods=['GET'])
def get_maintenance(maintenance_id):
    response, status_code = MaintenanceController.get_maintenance(maintenance_id)
    return jsonify(response), status_code

@maintenance_blueprint.route('/maintenances', methods=['GET'])
def get_all_maintenances():
    response, status_code = MaintenanceController.get_all_maintenances()
    return jsonify(response), status_code

@maintenance_blueprint.route('/maintenances/<int:maintenance_id>', methods=['PUT'])
def update_maintenance(maintenance_id):
    data = request.json
    response, status_code = MaintenanceController.update_maintenance(maintenance_id, data)
    return jsonify(response), status_code

@maintenance_blueprint.route('/maintenances/<int:maintenance_id>', methods=['DELETE'])
def delete_maintenance(maintenance_id):
    response, status_code = MaintenanceController.delete_maintenance(maintenance_id)
    return jsonify(response), status_code
