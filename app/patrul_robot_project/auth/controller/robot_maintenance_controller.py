from auth.service.robot_maintenance_service import RobotMaintenanceService

class RobotMaintenanceController:

    @staticmethod
    def get_maintenances_for_robot(robot_id):
        maintenances = RobotMaintenanceService.get_maintenances_for_robot(robot_id)
        return [{
            'maintenance_id': maintenance.maintenance.maintenance_id,
            'description': maintenance.maintenance.description,
            # Додайте інші поля, які хочете вивести
        } for maintenance in maintenances], 200

    @staticmethod
    def get_all_maintenances_with_robots():
        maintenances = RobotMaintenanceService.get_all_maintenances_with_robots()
        return [{
            'maintenance_id': maintenance.maintenance_id,
            'description': maintenance.description,
            'robots': [
                {
                    'robot_id': robot_maintenance.robot.robot_id,
                    'status': robot_maintenance.robot.status,
                    'max_distance': robot_maintenance.robot.max_distance
                    # Додайте інші поля, які хочете вивести
                } for robot_maintenance in maintenance.robot_maintenances
            ]
        } for maintenance in maintenances], 200

    @staticmethod
    def get_maintenance_with_robots(maintenance_id):
        maintenance, robots = RobotMaintenanceService.get_maintenance_with_robots(maintenance_id)
        if maintenance:
            return {
                'maintenance_id': maintenance.maintenance_id,
                'description': maintenance.description,  # Ось тут ми звертаємося до опису
                'robots': [
                    {
                        'robot_id': robot.robot_id,
                        'status': robot.status,
                        'max_distance': robot.max_distance
                    } for robot in robots
                ]
            }, 200
        return {'error': 'Maintenance not found'}, 404
