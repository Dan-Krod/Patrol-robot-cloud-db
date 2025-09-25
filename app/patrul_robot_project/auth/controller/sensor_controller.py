from auth.service.sensor_service import SensorService

class SensorController:

    @staticmethod
    def add_sensor(data):
        required_fields = ['robot_id', 'technology_used', 'detection_range', 'trigger_status']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400
        
        sensor = SensorService.add_sensor(
            robot_id=data['robot_id'],
            technology_used=data['technology_used'],
            detection_range=data['detection_range'],
            trigger_status=data['trigger_status']
        )
        return {'id': sensor.sensor_id}, 201

    @staticmethod
    def get_sensor(sensor_id):
        sensor = SensorService.get_sensor(sensor_id)
        if sensor:
            return {
                'id': sensor.sensor_id,
                'robot_id': sensor.robot_id,
                'technology_used': sensor.technology_used,
                'detection_range': sensor.detection_range,
                'trigger_status': sensor.trigger_status
            }, 200
        return {'error': 'Sensor not found'}, 404

    @staticmethod
    def get_all_sensors():
        sensors = SensorService.get_all_sensors()
        return [{
            'id': sensor.sensor_id,
            'robot_id': sensor.robot_id,
            'technology_used': sensor.technology_used,
            'detection_range': sensor.detection_range,
            'trigger_status': sensor.trigger_status
        } for sensor in sensors], 200

    @staticmethod
    def update_sensor(sensor_id, data):
        required_fields = ['robot_id', 'technology_used', 'detection_range', 'trigger_status']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400

        sensor = SensorService.update_sensor(
            sensor_id,
            robot_id=data['robot_id'],
            technology_used=data['technology_used'],
            detection_range=data['detection_range'],
            trigger_status=data['trigger_status']
        )
        if sensor:
            return {'message': 'Sensor updated'}, 200
        return {'error': 'Sensor not found'}, 404

    @staticmethod
    def delete_sensor(sensor_id):
        sensor = SensorService.delete_sensor(sensor_id)
        if sensor:
            return {'message': 'Sensor deleted'}, 200
        return {'error': 'Sensor not found'}, 404

    @staticmethod
    def get_sensors_with_robot():
        sensors = SensorService.get_all_sensors_with_robot()
        return [{
            'id': sen.sensor_id,
            'technology_used': sen.technology_used,
            'detection_range': sen.detection_range,
            'robot_id': sen.robot.robot_id if sen.robot else None,
            'robot_status': sen.robot.status if sen.robot else None
        } for sen in sensors], 200
