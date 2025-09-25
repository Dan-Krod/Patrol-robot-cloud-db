from auth.domain.models import db
from auth.domain.battery import Battery

class BatteryDAO:
    @staticmethod
    def add_battery(log_time, battery_level, robot_id, temperature):
        new_battery = Battery(log_time=log_time, battery_level=battery_level, robot_id=robot_id, temperature=temperature)
        db.session.add(new_battery)
        db.session.commit()
        return new_battery

    @staticmethod
    def get_battery(battery_id):
        return Battery.query.get(battery_id)

    @staticmethod
    def get_all_batteries():
        return Battery.query.all()

    @staticmethod
    def update_battery(battery_id, log_time, battery_level, robot_id, temperature):
        battery = Battery.query.get(battery_id)
        if battery:
            battery.log_time = log_time
            battery.battery_level = battery_level
            battery.robot_id = robot_id
            battery.temperature = temperature
            db.session.commit()
        return battery

    @staticmethod
    def delete_battery(battery_id):
        battery = Battery.query.get(battery_id)
        if battery:
            db.session.delete(battery)
            db.session.commit()
        return battery
