from auth.dao.patrol_report_dao import PatrolReportDAO

class PatrolReportService:
    @staticmethod
    def add_report(start_time, end_time, observations, person_detected, routes_id):
        return PatrolReportDAO.add_report(start_time, end_time, observations, person_detected, routes_id)

    @staticmethod
    def get_report(report_id):
        return PatrolReportDAO.get_report(report_id)

    @staticmethod
    def get_all_reports():
        return PatrolReportDAO.get_all_reports()

    @staticmethod
    def update_report(report_id, start_time, end_time, observations, person_detected, routes_id):
        return PatrolReportDAO.update_report(report_id, start_time, end_time, observations, person_detected, routes_id)

    @staticmethod
    def delete_report(report_id):
        return PatrolReportDAO.delete_report(report_id)