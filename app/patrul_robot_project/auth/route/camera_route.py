from flask import Blueprint, request, jsonify
from auth.controller.camera_controller import CameraController

camera_blueprint = Blueprint('camera', __name__)


@camera_blueprint.route('/cameras', methods=['POST'])
def add_camera():
    """
    Add a new camera
    ---
    tags:
      - Camera
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - model
            - resolution
          properties:
            model:
              type: string
              example: "Logitech C920"
            resolution:
              type: string
              example: "1920x1080"
    responses:
      201:
        description: Camera created successfully
      400:
        description: Invalid input
    """
    data = request.json
    response, status_code = CameraController.add_camera(data)
    return jsonify(response), status_code


@camera_blueprint.route('/cameras/<int:camera_id>', methods=['GET'])
def get_camera(camera_id):
    """
    Get a camera by ID
    ---
    tags:
      - Camera
    parameters:
      - name: camera_id
        in: path
        required: true
        type: integer
        description: ID of the camera
    responses:
      200:
        description: Camera data
      404:
        description: Camera not found
    """
    response, status_code = CameraController.get_camera(camera_id)
    return jsonify(response), status_code


@camera_blueprint.route('/cameras', methods=['GET'])
def get_all_cameras():
    """
    Get all cameras
    ---
    tags:
      - Camera
    responses:
      200:
        description: List of all cameras
    """
    response, status_code = CameraController.get_all_cameras()
    return jsonify(response), status_code


@camera_blueprint.route('/cameras/<int:camera_id>', methods=['PUT'])
def update_camera(camera_id):
    """
    Update a camera
    ---
    tags:
      - Camera
    consumes:
      - application/json
    parameters:
      - name: camera_id
        in: path
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            model:
              type: string
              example: "Logitech Brio"
            resolution:
              type: string
              example: "3840x2160"
    responses:
      200:
        description: Camera updated successfully
      404:
        description: Camera not found
    """
    data = request.json
    response, status_code = CameraController.update_camera(camera_id, data)
    return jsonify(response), status_code


@camera_blueprint.route('/cameras/<int:camera_id>', methods=['DELETE'])
def delete_camera(camera_id):
    """
    Delete a camera
    ---
    tags:
      - Camera
    parameters:
      - name: camera_id
        in: path
        required: true
        type: integer
        description: ID of the camera
    responses:
      200:
        description: Camera deleted successfully
      404:
        description: Camera not found
    """
    response, status_code = CameraController.delete_camera(camera_id)
    return jsonify(response), status_code
