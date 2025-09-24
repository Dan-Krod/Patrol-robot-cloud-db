from auth.dao.camera_dao import CameraDAO

class CameraService:
    @staticmethod
    def add_camera(robot_id, resolution, zoom_level, status, night_vision, panoramic_view):
        return CameraDAO.add_camera(robot_id, resolution, zoom_level, status, night_vision, panoramic_view)

    @staticmethod
    def get_camera(camera_id):
        return CameraDAO.get_camera(camera_id)

    @staticmethod
    def get_all_cameras():
        return CameraDAO.get_all_cameras()

    @staticmethod
    def update_camera(camera_id, robot_id, resolution, zoom_level, status, night_vision, panoramic_view):
        return CameraDAO.update_camera(camera_id, robot_id, resolution, zoom_level, status, night_vision, panoramic_view)

    @staticmethod
    def delete_camera(camera_id):
        return CameraDAO.delete_camera(camera_id)
