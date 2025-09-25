from auth.dao.operator_dao import OperatorDAO

class OperatorService:
    @staticmethod
    def add_operator(name, shift_start, shift_end, contact_info):
        return OperatorDAO.add_operator(name, shift_start, shift_end, contact_info)

    @staticmethod
    def get_operator(operator_id):
        return OperatorDAO.get_operator(operator_id)

    @staticmethod
    def get_all_operators():
        return OperatorDAO.get_all_operators()

    @staticmethod
    def update_operator(operator_id, name, shift_start, shift_end, contact_info):
        return OperatorDAO.update_operator(operator_id, name, shift_start, shift_end, contact_info)

    @staticmethod
    def delete_operator(operator_id):
        return OperatorDAO.delete_operator(operator_id)

    def get_all_operators_with_robots():
        return OperatorDAO.get_all_operators_with_robots()