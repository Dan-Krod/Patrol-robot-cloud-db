from auth.domain.models import db
from auth.domain.robot import Robot

class RobotDAO:
    @staticmethod
    def add_robot(status, max_distance, operator_id, station_id, alternative_power_source):
        new_robot = Robot(status=status, max_distance=max_distance, operator_id=operator_id, station_id=station_id, alternative_power_source=alternative_power_source)
        db.session.add(new_robot)
        db.session.commit()
        return new_robot

    @staticmethod
    def get_robot(robot_id):
        return Robot.query.get(robot_id)

    @staticmethod
    def get_all_robots():
        return Robot.query.all()

    @staticmethod
    def update_robot(robot_id, status, max_distance, operator_id, station_id, alternative_power_source):
        robot = Robot.query.get(robot_id)
        if robot:
            robot.status = status
            robot.max_distance = max_distance
            robot.operator_id = operator_id
            robot.station_id = station_id
            robot.alternative_power_source = alternative_power_source
            db.session.commit()
        return robot

    @staticmethod
    def delete_robot(robot_id):
        robot = Robot.query.get(robot_id)
        if robot:
            db.session.delete(robot)
            db.session.commit()
        return robot
