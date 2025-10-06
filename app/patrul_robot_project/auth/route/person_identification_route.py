from flask import Blueprint, request, jsonify
from auth.controller.person_identification_controller import PersonIdentificationController

person_identification_blueprint = Blueprint('person_identification', __name__)


@person_identification_blueprint.route('/person_identifications', methods=['POST'])
def add_identification():
    """
    Add a new person identification record
    ---
    tags:
      - Person Identification
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - person_name
            - timestamp
            - accuracy
            - sensor_id
            - camera_id
            - report_id
          properties:
            person_name:
              type: string
              example: "John Doe"
            timestamp:
              type: string
              format: date-time
              example: "2025-10-03T14:30:00"
            accuracy:
              type: number
              format: float
              example: 97.85
            sensor_id:
              type: integer
              example: 1
            camera_id:
              type: integer
              example: 2
            report_id:
              type: integer
              example: 3
    responses:
      201:
        description: Person identification record created successfully
      400:
        description: Invalid input
    """
    data = request.json
    response, status_code = PersonIdentificationController.add_identification(data)
    return jsonify(response), status_code


@person_identification_blueprint.route('/person_identifications/<int:identification_id>', methods=['GET'])
def get_identification(identification_id):
    """
    Get a person identification record by ID
    ---
    tags:
      - Person Identification
    parameters:
      - name: identification_id
        in: path
        required: true
        type: integer
        description: ID of the person identification record
    responses:
      200:
        description: Person identification record data
      404:
        description: Person identification record not found
    """
    response, status_code = PersonIdentificationController.get_identification(identification_id)
    return jsonify(response), status_code


@person_identification_blueprint.route('/person_identifications', methods=['GET'])
def get_all_identifications():
    """
    Get all person identification records
    ---
    tags:
      - Person Identification
    responses:
      200:
        description: List of all person identifications
    """
    response, status_code = PersonIdentificationController.get_all_identifications()
    return jsonify(response), status_code


@person_identification_blueprint.route('/person_identifications/<int:identification_id>', methods=['PUT'])
def update_identification(identification_id):
    """
    Update a person identification record
    ---
    tags:
      - Person Identification
    consumes:
      - application/json
    parameters:
      - name: identification_id
        in: path
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            person_name:
              type: string
              example: "Jane Smith"
            timestamp:
              type: string
              format: date-time
              example: "2025-11-01T09:15:00"
            accuracy:
              type: number
              format: float
              example: 95.40
            sensor_id:
              type: integer
              example: 1
            camera_id:
              type: integer
              example: 2
            report_id:
              type: integer
              example: 3
    responses:
      200:
        description: Person identification record updated successfully
      404:
        description: Person identification record not found
    """
    data = request.json
    response, status_code = PersonIdentificationController.update_identification(identification_id, data)
    return jsonify(response), status_code


@person_identification_blueprint.route('/person_identifications/<int:identification_id>', methods=['DELETE'])
def delete_identification(identification_id):
    """
    Delete a person identification record
    ---
    tags:
      - Person Identification
    parameters:
      - name: identification_id
        in: path
        required: true
        type: integer
        description: ID of the person identification record
    responses:
      200:
        description: Person identification record deleted successfully
      404:
        description: Person identification record not found
    """
    response, status_code = PersonIdentificationController.delete_identification(identification_id)
    return jsonify(response), status_code


@person_identification_blueprint.route('/person_identifications_with_reports', methods=['GET'])
def get_person_identifications_with_reports():
    """
    Get all person identifications with linked reports
    ---
    tags:
      - Person Identification
    responses:
      200:
        description: List of person identifications with related reports
    """
    response, status_code = PersonIdentificationController.get_person_identifications_with_reports()
    return jsonify(response), status_code
