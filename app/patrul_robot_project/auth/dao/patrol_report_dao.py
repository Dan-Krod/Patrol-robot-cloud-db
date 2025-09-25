from auth.domain.models import db
from auth.domain.patrol_report import PatrolReport

class PatrolReportDAO:
    @staticmethod
    def add_report(start_time, end_time, observations, person_detected, routes_id):
        new_report = PatrolReport(start_time=start_time, end_time=end_time, observations=observations, person_detected=person_detected, routes_id=routes_id)
        db.session.add(new_report)
        db.session.commit()
        return new_report

    @staticmethod
    def get_report(report_id):
        return PatrolReport.query.get(report_id)

    @staticmethod
    def get_all_reports():
        return PatrolReport.query.all()

    @staticmethod
    def update_report(report_id, start_time, end_time, observations, person_detected, routes_id):
        report = PatrolReport.query.get(report_id)
        if report:
            report.start_time = start_time
            report.end_time = end_time
            report.observations = observations
            report.person_detected = person_detected
            report.routes_id = routes_id
            db.session.commit()
        return report

    @staticmethod
    def delete_report(report_id):
        report = PatrolReport.query.get(report_id)
        if report:
            db.session.delete(report)
            db.session.commit()
        return report
