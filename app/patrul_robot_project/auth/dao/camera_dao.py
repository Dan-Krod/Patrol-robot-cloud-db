from auth.domain.models import db
from auth.domain.camera import Camera

class CameraDAO:
    @staticmethod
    def add_camera(robot_id, resolution, zoom_level, status, night_vision, panoramic_view):
        new_camera = Camera(robot_id=robot_id, resolution=resolution, zoom_level=zoom_level, status=status, night_vision=night_vision, panoramic_view=panoramic_view)
        db.session.add(new_camera)
        db.session.commit()
        return new_camera

    @staticmethod
    def get_camera(camera_id):
        return Camera.query.get(camera_id)

    @staticmethod
    def get_all_cameras():
        return Camera.query.all()

    @staticmethod
    def update_camera(camera_id, robot_id, resolution, zoom_level, status, night_vision, panoramic_view):
        camera = Camera.query.get(camera_id)
        if camera:
            camera.robot_id = robot_id
            camera.resolution = resolution
            camera.zoom_level = zoom_level
            camera.status = status
            camera.night_vision = night_vision
            camera.panoramic_view = panoramic_view
            db.session.commit()
        return camera

    @staticmethod
    def delete_camera(camera_id):
        camera = Camera.query.get(camera_id)
        if camera:
            db.session.delete(camera)
            db.session.commit()
        return camera
