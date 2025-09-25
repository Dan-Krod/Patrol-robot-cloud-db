from auth.dao.robot_maintenance_dao import RobotMaintenanceDAO

class RobotMaintenanceService:
    @staticmethod
    def add_robot_maintenance(robot_id, maintenance_id):
        """Додає запис про техобслуговування для робота."""
        return RobotMaintenanceDAO.add_robot_maintenance(robot_id, maintenance_id)

    @staticmethod
    def get_all_robot_maintenances():
        """Отримує всі записи про техобслуговування."""
        return RobotMaintenanceDAO.get_all_robot_maintenances()

    @staticmethod
    def get_maintenances_for_robot(robot_id):
        """Отримує техобслуговування для конкретного робота."""
        return RobotMaintenanceDAO.get_maintenances_for_robot(robot_id)

    @staticmethod
    def get_all_maintenances_with_robots():
        """Отримує всі техобслуговування разом з роботами, які їх виконують."""
        return RobotMaintenanceDAO.get_all_maintenances_with_robots()

    @staticmethod
    def get_maintenance_with_robots(maintenance_id):
        return RobotMaintenanceDAO.get_maintenance_with_robots(maintenance_id)