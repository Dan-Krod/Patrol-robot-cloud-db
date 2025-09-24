from auth.domain.models import db
from auth.domain.operator import Operator

class OperatorDAO:
    @staticmethod
    def add_operator(name, shift_start, shift_end, contact_info):
        new_operator = Operator(name=name, shift_start=shift_start, shift_end=shift_end, contact_info=contact_info)
        db.session.add(new_operator)
        db.session.commit()
        return new_operator

    @staticmethod
    def get_operator(operator_id):
        return Operator.query.get(operator_id)

    @staticmethod
    def get_all_operators():
        return Operator.query.all()

    @staticmethod
    def update_operator(operator_id, name, shift_start, shift_end, contact_info):
        operator = Operator.query.get(operator_id)
        if operator:
            operator.name = name
            operator.shift_start = shift_start
            operator.shift_end = shift_end
            operator.contact_info = contact_info
            db.session.commit()
        return operator

    @staticmethod
    def delete_operator(operator_id):
        operator = Operator.query.get(operator_id)
        if operator:
            db.session.delete(operator)
            db.session.commit()
        return operator

    def get_all_operators_with_robots():
        return Operator.query.options(db.joinedload(Operator.robots)).all()