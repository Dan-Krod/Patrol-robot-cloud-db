from flask import Blueprint, request, jsonify
from auth.controller.operator_controller import OperatorController

operator_blueprint = Blueprint('operator', __name__)


@operator_blueprint.route('/operators', methods=['POST'])
def add_operator():
    """
    Add a new operator
    ---
    tags:
      - Operator
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - shift_start
            - shift_end
            - contact_info
          properties:
            name:
              type: string
              example: John Doe
            shift_start:
              type: string
              format: time
              example: "08:00:00"
            shift_end:
              type: string
              format: time
              example: "16:00:00"
            contact_info:
              type: string
              example: "+380991234567"
    responses:
      201:
        description: Operator created successfully
      400:
        description: Invalid input
    """
    data = request.json
    response, status_code = OperatorController.add_operator(data)
    return jsonify(response), status_code


@operator_blueprint.route('/operators/<int:operator_id>', methods=['GET'])
def get_operator(operator_id):
    """
    Get an operator by ID
    ---
    tags:
      - Operator
    parameters:
      - name: operator_id
        in: path
        required: true
        type: integer
        description: ID of the operator
    responses:
      200:
        description: Operator data
      404:
        description: Operator not found
    """
    response, status_code = OperatorController.get_operator(operator_id)
    return jsonify(response), status_code


@operator_blueprint.route('/operators', methods=['GET'])
def get_all_operators():
    """
    Get all operators
    ---
    tags:
      - Operator
    responses:
      200:
        description: List of all operators with their details
    """
    response, status_code = OperatorController.get_all_operators()
    return jsonify(response), status_code


@operator_blueprint.route('/operators/<int:operator_id>', methods=['PUT'])
def update_operator(operator_id):
    """
    Update an operator
    ---
    tags:
      - Operator
    consumes:
      - application/json
    parameters:
      - name: operator_id
        in: path
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Jane Doe
            shift_start:
              type: string
              format: time
              example: "09:00:00"
            shift_end:
              type: string
              format: time
              example: "17:00:00"
            contact_info:
              type: string
              example: "+380671234567"
    responses:
      200:
        description: Operator updated successfully
      404:
        description: Operator not found
    """
    data = request.json
    response, status_code = OperatorController.update_operator(operator_id, data)
    return jsonify(response), status_code


@operator_blueprint.route('/operators/<int:operator_id>', methods=['DELETE'])
def delete_operator(operator_id):
    """
    Delete an operator
    ---
    tags:
      - Operator
    parameters:
      - name: operator_id
        in: path
        required: true
        type: integer
        description: ID of the operator
    responses:
      200:
        description: Operator deleted successfully
      404:
        description: Operator not found
    """
    response, status_code = OperatorController.delete_operator(operator_id)
    return jsonify(response), status_code


@operator_blueprint.route('/operators_with_robots', methods=['GET'])
def get_operators_with_robots():
    """
    Get operators with their assigned robots
    ---
    tags:
      - Operator
    responses:
      200:
        description: List of operators with their robots, including shift details and contact info
    """
    response, status_code = OperatorController.get_operators_with_robots()
    return jsonify(response), status_code
