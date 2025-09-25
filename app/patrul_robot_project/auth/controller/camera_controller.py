from auth.service.camera_service import CameraService

class CameraController:

    @staticmethod
    def add_camera(data):
        required_fields = ['robot_id', 'resolution', 'zoom_level', 'status', 'night_vision', 'panoramic_view']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400
        
        camera = CameraService.add_camera(
            robot_id=data['robot_id'],
            resolution=data['resolution'],
            zoom_level=data['zoom_level'],
            status=data['status'],
            night_vision=data['night_vision'],
            panoramic_view=data['panoramic_view']
        )
        return {'id': camera.camera_id}, 201

    @staticmethod
    def get_camera(camera_id):
        camera = CameraService.get_camera(camera_id)
        if camera:
            return {
                'id': camera.camera_id,
                'robot_id': camera.robot_id,
                'resolution': camera.resolution,
                'zoom_level': camera.zoom_level,
                'status': camera.status,
                'night_vision': camera.night_vision,
                'panoramic_view': camera.panoramic_view
            }, 200
        return {'error': 'Camera not found'}, 404

    @staticmethod
    def get_all_cameras():
        cameras = CameraService.get_all_cameras()
        return [{
            'id': cam.camera_id,
            'robot_id': cam.robot_id,
            'resolution': cam.resolution,
            'zoom_level': cam.zoom_level,
            'status': cam.status,
            'night_vision': cam.night_vision,
            'panoramic_view': cam.panoramic_view
        } for cam in cameras], 200

    @staticmethod
    def update_camera(camera_id, data):
        required_fields = ['robot_id', 'resolution', 'zoom_level', 'status', 'night_vision', 'panoramic_view']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400

        camera = CameraService.update_camera(
            camera_id,
            robot_id=data['robot_id'],
            resolution=data['resolution'],
            zoom_level=data['zoom_level'],
            status=data['status'],
            night_vision=data['night_vision'],
            panoramic_view=data['panoramic_view']
        )
        if camera:
            return {'message': 'Camera updated'}, 200
        return {'error': 'Camera not found'}, 404

    @staticmethod
    def delete_camera(camera_id):
        camera = CameraService.delete_camera(camera_id)
        if camera:
            return {'message': 'Camera deleted'}, 200
        return {'error': 'Camera not found'}, 404
