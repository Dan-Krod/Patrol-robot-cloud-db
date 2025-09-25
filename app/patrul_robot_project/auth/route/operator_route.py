from flask import Blueprint, request, jsonify
from auth.controller.operator_controller import OperatorController

operator_blueprint = Blueprint('operator', __name__)

@operator_blueprint.route('/operators', methods=['POST'])
def add_operator():
    data = request.json
    response, status_code = OperatorController.add_operator(data)
    return jsonify(response), status_code

@operator_blueprint.route('/operators/<int:operator_id>', methods=['GET'])
def get_operator(operator_id):
    response, status_code = OperatorController.get_operator(operator_id)
    return jsonify(response), status_code

@operator_blueprint.route('/operators', methods=['GET'])
def get_all_operators():
    response, status_code = OperatorController.get_all_operators()
    return jsonify(response), status_code

@operator_blueprint.route('/operators/<int:operator_id>', methods=['PUT'])
def update_operator(operator_id):
    data = request.json
    response, status_code = OperatorController.update_operator(operator_id, data)
    return jsonify(response), status_code

@operator_blueprint.route('/operators/<int:operator_id>', methods=['DELETE'])
def delete_operator(operator_id):
    response, status_code = OperatorController.delete_operator(operator_id)
    return jsonify(response), status_code

@operator_blueprint.route('/operators_with_robots', methods=['GET'])
def get_operators_with_robots():
    response, status_code = OperatorController.get_operators_with_robots()
    return jsonify(response), status_code
