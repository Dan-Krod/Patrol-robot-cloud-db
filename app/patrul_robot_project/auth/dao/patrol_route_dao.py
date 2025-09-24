from auth.domain.models import db
from auth.domain.patrol_route import PatrolRoute

class PatrolRouteDAO:
    @staticmethod
    def add_route(start_point, end_point, difficulty_level, robot_id):
        new_route = PatrolRoute(start_point=start_point, end_point=end_point, difficulty_level=difficulty_level, robot_id=robot_id)
        db.session.add(new_route)
        db.session.commit()
        return new_route

    @staticmethod
    def get_route(routes_id):
        return PatrolRoute.query.get(routes_id)

    @staticmethod
    def get_all_routes():
        return PatrolRoute.query.all()

    @staticmethod
    def update_route(routes_id, start_point, end_point, difficulty_level, robot_id):
        route = PatrolRoute.query.get(routes_id)
        if route:
            route.start_point = start_point
            route.end_point = end_point
            route.difficulty_level = difficulty_level
            route.robot_id = robot_id
            db.session.commit()
        return route

    @staticmethod
    def delete_route(routes_id):
        route = PatrolRoute.query.get(routes_id)
        if route:
            db.session.delete(route)
            db.session.commit()
        return route

    