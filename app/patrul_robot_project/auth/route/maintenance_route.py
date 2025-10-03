from flask import Blueprint, request, jsonify
from auth.controller.maintenance_controller import MaintenanceController

maintenance_blueprint = Blueprint('maintenance', __name__)


@maintenance_blueprint.route('/maintenances', methods=['POST'])
def add_maintenance():
    """
    Add a new maintenance record
    ---
    tags:
      - Maintenance
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - robot_id
            - description
            - scheduled_date
          properties:
            robot_id:
              type: integer
              example: 1
            description:
              type: string
              example: "Battery replacement"
            scheduled_date:
              type: string
              format: date
              example: "2025-10-15"
    responses:
      201:
        description: Maintenance record created successfully
      400:
        description: Invalid input
    """
    data = request.json
    response, status_code = MaintenanceController.add_maintenance(data)
    return jsonify(response), status_code


@maintenance_blueprint.route('/maintenances/<int:maintenance_id>', methods=['GET'])
def get_maintenance(maintenance_id):
    """
    Get a maintenance record by ID
    ---
    tags:
      - Maintenance
    parameters:
      - name: maintenance_id
        in: path
        required: true
        type: integer
        description: ID of the maintenance record
    responses:
      200:
        description: Maintenance record data
      404:
        description: Maintenance record not found
    """
    response, status_code = MaintenanceController.get_maintenance(maintenance_id)
    return jsonify(response), status_code


@maintenance_blueprint.route('/maintenances', methods=['GET'])
def get_all_maintenances():
    """
    Get all maintenance records
    ---
    tags:
      - Maintenance
    responses:
      200:
        description: List of all maintenance records
    """
    response, status_code = MaintenanceController.get_all_maintenances()
    return jsonify(response), status_code


@maintenance_blueprint.route('/maintenances/<int:maintenance_id>', methods=['PUT'])
def update_maintenance(maintenance_id):
    """
    Update a maintenance record
    ---
    tags:
      - Maintenance
    consumes:
      - application/json
    parameters:
      - name: maintenance_id
        in: path
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            description:
              type: string
              example: "Software update"
            scheduled_date:
              type: string
              format: date
              example: "2025-11-01"
    responses:
      200:
        description: Maintenance record updated successfully
      404:
        description: Maintenance record not found
    """
    data = request.json
    response, status_code = MaintenanceController.update_maintenance(maintenance_id, data)
    return jsonify(response), status_code


@maintenance_blueprint.route('/maintenances/<int:maintenance_id>', methods=['DELETE'])
def delete_maintenance(maintenance_id):
    """
    Delete a maintenance record
    ---
    tags:
      - Maintenance
    parameters:
      - name: maintenance_id
        in: path
        required: true
        type: integer
        description: ID of the maintenance record
    responses:
      200:
        description: Maintenance record deleted successfully
      404:
        description: Maintenance record not found
    """
    response, status_code = MaintenanceController.delete_maintenance(maintenance_id)
    return jsonify(response), status_code