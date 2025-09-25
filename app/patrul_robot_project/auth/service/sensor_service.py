from auth.dao.sensor_dao import SensorDAO

class SensorService:
    @staticmethod
    def add_sensor(robot_id, technology_used, detection_range, trigger_status):
        return SensorDAO.add_sensor(robot_id, technology_used, detection_range, trigger_status)

    @staticmethod
    def get_sensor(sensor_id):
        return SensorDAO.get_sensor(sensor_id)

    @staticmethod
    def get_all_sensors():
        return SensorDAO.get_all_sensors()

    @staticmethod
    def update_sensor(sensor_id, robot_id, technology_used, detection_range, trigger_status):
        return SensorDAO.update_sensor(sensor_id, robot_id, technology_used, detection_range, trigger_status)

    @staticmethod
    def delete_sensor(sensor_id):
        return SensorDAO.delete_sensor(sensor_id)
    
    @staticmethod
    def get_all_sensors_with_robot():
        return SensorDAO.get_all_sensors_with_robot()
