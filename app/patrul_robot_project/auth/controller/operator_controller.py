from auth.service.operator_service import OperatorService

class OperatorController:

    @staticmethod
    def add_operator(data):
        required_fields = ['name', 'shift_start', 'shift_end', 'contact_info']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400
        
        operator = OperatorService.add_operator(
            name=data['name'],
            shift_start=data['shift_start'],
            shift_end=data['shift_end'],
            contact_info=data['contact_info']
        )
        return {'id': operator.operators_id}, 201

    @staticmethod
    def get_operator(operator_id):
        operator = OperatorService.get_operator(operator_id)
        if operator:
            return {
                'id': operator.operators_id,
                'name': operator.name,
                'shift_start': operator.shift_start.strftime('%H:%M:%S'),
                'shift_end': operator.shift_end.strftime('%H:%M:%S'),
                'contact_info': operator.contact_info
            }, 200
        return {'error': 'Operator not found'}, 404

    @staticmethod
    def get_all_operators():
        operators = OperatorService.get_all_operators()
        return [{
            'id': op.operators_id,
            'name': op.name,
            'shift_start': op.shift_start.strftime('%H:%M:%S'),
            'shift_end': op.shift_end.strftime('%H:%M:%S'),
            'contact_info': op.contact_info
        } for op in operators], 200

    @staticmethod
    def update_operator(operator_id, data):
        required_fields = ['name', 'shift_start', 'shift_end', 'contact_info']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400

        operator = OperatorService.update_operator(
            operator_id,
            name=data['name'],
            shift_start=data['shift_start'],
            shift_end=data['shift_end'],
            contact_info=data['contact_info']
        )
        if operator:
            return {'message': 'Operator updated'}, 200
        return {'error': 'Operator not found'}, 404

    @staticmethod
    def delete_operator(operator_id):
        operator = OperatorService.delete_operator(operator_id)
        if operator:
            return {'message': 'Operator deleted'}, 200
        return {'error': 'Operator not found'}, 404

    @staticmethod
    def get_operators_with_robots():
        operators = OperatorService.get_all_operators_with_robots()
        return [{
            'id': op.operators_id,
            'name': op.name,
            'shift_start': op.shift_start.strftime('%H:%M:%S'),
            'shift_end': op.shift_end.strftime('%H:%M:%S'),
            'contact_info': op.contact_info,
            'robots': [{
                'id': rb.robot_id,
                'status': rb.status,
                'max_distance': rb.max_distance,
                'alternative_power_source': rb.alternative_power_source
            } for rb in op.robots]
        } for op in operators], 200
