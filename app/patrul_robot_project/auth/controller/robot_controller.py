from auth.service.robot_service import RobotService

class RobotController:

    @staticmethod
    def add_robot(data):
        required_fields = ['status', 'max_distance', 'operator_id', 'station_id', 'alternative_power_source']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400
        
        alt_power = data['alternative_power_source']
        if isinstance(alt_power, bool):
            alt_power = 'yes' if alt_power else 'no'

        robot = RobotService.add_robot(
            status=data['status'],
            max_distance=data['max_distance'],
            operator_id=data['operator_id'],
            station_id=data['station_id'],
            alternative_power_source=alt_power
        )
        return {'id': robot.robot_id}, 201

    @staticmethod
    def get_robot(robot_id):
        robot = RobotService.get_robot(robot_id)
        if robot:
            return {
                'id': robot.robot_id,
                'status': robot.status,
                'max_distance': robot.max_distance,
                'operator_id': robot.operator_id,
                'station_id': robot.station_id,
                'alternative_power_source': robot.alternative_power_source
            }, 200
        return {'error': 'Robot not found'}, 404

    @staticmethod
    def get_all_robots():
        robots = RobotService.get_all_robots()
        return [{
            'id': rb.robot_id,
            'status': rb.status,
            'max_distance': rb.max_distance,
            'operator_id': rb.operator_id,
            'station_id': rb.station_id,
            'alternative_power_source': rb.alternative_power_source
        } for rb in robots], 200

    @staticmethod
    def update_robot(robot_id, data):
        required_fields = ['status', 'max_distance', 'operator_id', 'station_id', 'alternative_power_source']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400
	
        alt_power = data['alternative_power_source']
        if isinstance(alt_power, bool):
            alt_power = 'yes' if alt_power else 'no'        
        
        robot = RobotService.update_robot(
            robot_id,
            status=data['status'],
            max_distance=data['max_distance'],
            operator_id=data['operator_id'],
            station_id=data['station_id'],
            alternative_power_source=alt_power
        )
        if robot:
            return {'message': 'Robot updated'}, 200
        return {'error': 'Robot not found'}, 404

    @staticmethod
    def delete_robot(robot_id):
        robot = RobotService.delete_robot(robot_id)
        if robot:
            return {'message': 'Robot deleted'}, 200
        return {'error': 'Robot not found'}, 404
