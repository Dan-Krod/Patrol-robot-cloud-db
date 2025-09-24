from auth.domain.models import db
from auth.domain.robot_maintenance import RobotMaintenance
from auth.domain.maintance import Maintenance
from auth.domain.robot import Robot

class RobotMaintenanceDAO:
    @staticmethod
    def add_robot_maintenance(robot_id, maintenance_id):
        new_robot_maintenance = RobotMaintenance(
            robot_id=robot_id,
            maintenance_id=maintenance_id
        )
        db.session.add(new_robot_maintenance)
        db.session.commit()
        return new_robot_maintenance

    @staticmethod
    def get_all_robot_maintenances():
        return RobotMaintenance.query.all()

    @staticmethod
    def get_maintenances_for_robot(robot_id):
        return RobotMaintenance.query.filter_by(robot_id=robot_id).all()

    @staticmethod
    def get_all_maintenances_with_robots():
        maintenances = db.session.query(Maintenance).join(RobotMaintenance).join(Robot).all()
        return maintenances
    
    @staticmethod
    def get_maintenance_with_robots(maintenance_id):
        # Отримуємо техобслуговування за його id
        maintenance = Maintenance.query.get(maintenance_id)
        if not maintenance:
            return None, []

        # Отримуємо всіх роботів, пов'язаних з цим техобслуговуванням
        robots = [rm.robot for rm in maintenance.robot_maintenances]
        return maintenance, robots
