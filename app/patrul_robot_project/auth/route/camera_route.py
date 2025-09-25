from flask import Blueprint, request, jsonify
from auth.controller.camera_controller import CameraController

camera_blueprint = Blueprint('camera', __name__)

@camera_blueprint.route('/cameras', methods=['POST'])
def add_camera():
    data = request.json
    response, status_code = CameraController.add_camera(data)
    return jsonify(response), status_code

@camera_blueprint.route('/cameras/<int:camera_id>', methods=['GET'])
def get_camera(camera_id):
    response, status_code = CameraController.get_camera(camera_id)
    return jsonify(response), status_code

@camera_blueprint.route('/cameras', methods=['GET'])
def get_all_cameras():
    response, status_code = CameraController.get_all_cameras()
    return jsonify(response), status_code

@camera_blueprint.route('/cameras/<int:camera_id>', methods=['PUT'])
def update_camera(camera_id):
    data = request.json
    response, status_code = CameraController.update_camera(camera_id, data)
    return jsonify(response), status_code

@camera_blueprint.route('/cameras/<int:camera_id>', methods=['DELETE'])
def delete_camera(camera_id):
    response, status_code = CameraController.delete_camera(camera_id)
    return jsonify(response), status_code
