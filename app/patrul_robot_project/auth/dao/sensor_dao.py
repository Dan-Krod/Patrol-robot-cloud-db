from auth.domain.models import db
from auth.domain.sensor import Sensor

class SensorDAO:
    @staticmethod
    def add_sensor(robot_id, technology_used, detection_range, trigger_status):
        new_sensor = Sensor(robot_id=robot_id, technology_used=technology_used, detection_range=detection_range, trigger_status=trigger_status)
        db.session.add(new_sensor)
        db.session.commit()
        return new_sensor

    @staticmethod
    def get_sensor(sensor_id):
        return Sensor.query.get(sensor_id)

    @staticmethod
    def get_all_sensors():
        return Sensor.query.all()

    @staticmethod
    def update_sensor(sensor_id, robot_id, technology_used, detection_range, trigger_status):
        sensor = Sensor.query.get(sensor_id)
        if sensor:
            sensor.robot_id = robot_id
            sensor.technology_used = technology_used
            sensor.detection_range = detection_range
            sensor.trigger_status = trigger_status
            db.session.commit()
        return sensor

    @staticmethod
    def delete_sensor(sensor_id):
        sensor = Sensor.query.get(sensor_id)
        if sensor:
            db.session.delete(sensor)
            db.session.commit()
        return sensor

    @staticmethod
    def get_all_sensors_with_robot():
        return Sensor.query.options(db.joinedload(Sensor.robot)).all()