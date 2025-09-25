from auth.dao.robot_dao import RobotDAO

class RobotService:
    @staticmethod
    def add_robot(status, max_distance, operator_id, station_id, alternative_power_source):
        return RobotDAO.add_robot(status, max_distance, operator_id, station_id, alternative_power_source)

    @staticmethod
    def get_robot(robot_id):
        return RobotDAO.get_robot(robot_id)

    @staticmethod
    def get_all_robots():
        return RobotDAO.get_all_robots()

    @staticmethod
    def update_robot(robot_id, status, max_distance, operator_id, station_id, alternative_power_source):
        return RobotDAO.update_robot(robot_id, status, max_distance, operator_id, station_id, alternative_power_source)

    @staticmethod
    def delete_robot(robot_id):
        return RobotDAO.delete_robot(robot_id)
