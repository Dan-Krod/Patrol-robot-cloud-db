from flask import Blueprint, request, jsonify
from auth.controller.person_identification_controller import PersonIdentificationController

person_identification_blueprint = Blueprint('person_identification', __name__)

@person_identification_blueprint.route('/person_identifications', methods=['POST'])
def add_identification():
    data = request.json
    response, status_code = PersonIdentificationController.add_identification(data)
    return jsonify(response), status_code

@person_identification_blueprint.route('/person_identifications/<int:identification_id>', methods=['GET'])
def get_identification(identification_id):
    response, status_code = PersonIdentificationController.get_identification(identification_id)
    return jsonify(response), status_code

@person_identification_blueprint.route('/person_identifications', methods=['GET'])
def get_all_identifications():
    response, status_code = PersonIdentificationController.get_all_identifications()
    return jsonify(response), status_code

@person_identification_blueprint.route('/person_identifications/<int:identification_id>', methods=['PUT'])
def update_identification(identification_id):
    data = request.json
    response, status_code = PersonIdentificationController.update_identification(identification_id, data)
    return jsonify(response), status_code

@person_identification_blueprint.route('/person_identifications/<int:identification_id>', methods=['DELETE'])
def delete_identification(identification_id):
    response, status_code = PersonIdentificationController.delete_identification(identification_id)
    return jsonify(response), status_code

@person_identification_blueprint.route('/person_identifications_with_reports', methods=['GET'])
def get_person_identifications_with_reports():
    response, status_code = PersonIdentificationController.get_person_identifications_with_reports()
    return jsonify(response), status_code
