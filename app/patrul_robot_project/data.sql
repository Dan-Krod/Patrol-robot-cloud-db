-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `robot_db` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `robot_db` DEFAULT CHARACTER SET utf8mb3 ;
SHOW WARNINGS;
USE `robot_db` ;

-- -----------------------------------------------------
-- Table `operator`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `operator` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `operator` (
  `operators_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `shift_start` TIME NOT NULL,
  `shift_end` TIME NOT NULL,
  `contact_info` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`operators_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `charging_station`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `charging_station` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `charging_station` (
  `station_id` INT NOT NULL AUTO_INCREMENT,
  `location` VARCHAR(45) NOT NULL,
  `capacity` INT NOT NULL,
  `available` ENUM('yes', 'no') NOT NULL,
  PRIMARY KEY (`station_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `robot`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `robot` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `robot` (
  `robot_id` INT NOT NULL AUTO_INCREMENT,
  `status` VARCHAR(50) NOT NULL,
  `max_distance` INT NOT NULL,
  `operator_id` INT NOT NULL,
  `station_id` INT NOT NULL,
  `alternative_power_source` ENUM('yes', 'no') NOT NULL,
  PRIMARY KEY (`robot_id`),
  FOREIGN KEY (`operator_id`) REFERENCES `operator`(`operators_id`) ON DELETE CASCADE,
  FOREIGN KEY (`station_id`) REFERENCES `charging_station`(`station_id`) ON DELETE CASCADE
) ENGINE = InnoDB
AUTO_INCREMENT = 10
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `audio_system`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `audio_system` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `audio_system` (
  `audio_system_id` INT NOT NULL AUTO_INCREMENT,
  `has_speaker` ENUM('yes', 'no') NOT NULL,
  `has_microphone` ENUM('yes', 'no') NOT NULL,
  `has_panic_button` ENUM('yes', 'no') NOT NULL,
  `robot_id` INT NOT NULL,
  PRIMARY KEY (`audio_system_id`),
  FOREIGN KEY (`robot_id`) REFERENCES `robot`(`robot_id`) ON DELETE CASCADE
) ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `alert`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alert` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `alert` (
  `alerts_id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(50) NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `status` VARCHAR(50) NOT NULL,
  `audio_system_id` INT NOT NULL,
  PRIMARY KEY (`alerts_id`),
  FOREIGN KEY (`audio_system_id`) REFERENCES `audio_system`(`audio_system_id`) ON DELETE CASCADE
) ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `battery`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `battery` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `battery` (
  `battery_id` INT NOT NULL,
  `log_time` DATETIME NOT NULL,
  `battery_level` INT NOT NULL,
  `robot_id` INT NOT NULL,
  `temperature` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`battery_id`),
  FOREIGN KEY (`robot_id`) REFERENCES `robot`(`robot_id`) ON DELETE CASCADE
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `camera`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `camera` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `camera` (
  `camera_id` INT NOT NULL AUTO_INCREMENT,
  `robot_id` INT NOT NULL,
  `resolution` VARCHAR(45) NOT NULL,
  `zoom_level` INT NOT NULL,
  `status` VARCHAR(50) NOT NULL,
  `night_vision` ENUM('yes', 'no') NOT NULL,
  `panoramic_view` ENUM('yes', 'no') NOT NULL,
  PRIMARY KEY (`camera_id`),
  FOREIGN KEY (`robot_id`) REFERENCES `robot`(`robot_id`) ON DELETE CASCADE
) ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `maintenance`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `maintenance` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `maintenance` (
  `maintenance_id` INT NOT NULL AUTO_INCREMENT,
  `maintenance_date` DATETIME NOT NULL,
  `description` TEXT NOT NULL,
  `technician_name` VARCHAR(50) NOT NULL,
  `next_maintenance` DATETIME NOT NULL,
  PRIMARY KEY (`maintenance_id`)
) ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `patrol_route`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `patrol_route` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `patrol_route` (
  `routes_id` INT NOT NULL AUTO_INCREMENT,
  `start_point` VARCHAR(100) NOT NULL,
  `end_point` VARCHAR(100) NOT NULL,
  `difficulty_level` FLOAT NOT NULL,
  `robot_id` INT NOT NULL,
  PRIMARY KEY (`routes_id`),
  FOREIGN KEY (`robot_id`) REFERENCES `robot`(`robot_id`) ON DELETE CASCADE
) ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `patrol_report`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `patrol_report` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `patrol_report` (
  `report_id` INT NOT NULL AUTO_INCREMENT,
  `start_time` DATETIME NOT NULL,
  `end_time` DATETIME NOT NULL,
  `observations` TEXT NOT NULL,
  `person_detected` ENUM('yes', 'no') NOT NULL,
  `routes_id` INT NOT NULL,
  PRIMARY KEY (`report_id`),
  FOREIGN KEY (`routes_id`) REFERENCES `patrol_route`(`routes_id`) ON DELETE CASCADE
) ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `sensor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sensor` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `sensor` (
  `sensor_id` INT NOT NULL AUTO_INCREMENT,
  `robot_id` INT NOT NULL,
  `technology_used` VARCHAR(50) NOT NULL,
  `detection_range` INT NOT NULL,
  `trigger_status` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`sensor_id`),
  FOREIGN KEY (`robot_id`) REFERENCES `robot`(`robot_id`) ON DELETE CASCADE
) ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `person_identification`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `person_identification` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `person_identification` (
  `identification_id` INT NOT NULL AUTO_INCREMENT,
  `person_name` VARCHAR(50) NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `accuracy` DECIMAL(5,2) NOT NULL,
  `sensor_id` INT NOT NULL,
  `camera_id` INT NOT NULL,
  `report_id` INT NOT NULL,
  PRIMARY KEY (`identification_id`),
  FOREIGN KEY (`sensor_id`) REFERENCES `sensor`(`sensor_id`) ON DELETE CASCADE,
  FOREIGN KEY (`camera_id`) REFERENCES `camera`(`camera_id`) ON DELETE CASCADE,
  FOREIGN KEY (`report_id`) REFERENCES `patrol_report`(`report_id`) ON DELETE CASCADE
) ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb3;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `solar_system`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `solar_system` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `solar_system` (
  `solar_id` INT NOT NULL AUTO_INCREMENT,
  `status` VARCHAR(45) NOT NULL,
  `power_output` FLOAT NOT NULL,
  `technology_used` VARCHAR(45) NOT NULL,
  `station_id` INT NOT NULL,
  PRIMARY KEY (`solar_id`),
  FOREIGN KEY (`station_id`) REFERENCES `charging_station`(`station_id`) ON DELETE CASCADE
) ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb3;

COMMIT;

CREATE TABLE `robot_maintenance` (
    `robot_id` INT NOT NULL,
    `maintenance_id` INT NOT NULL,
    PRIMARY KEY (`robot_id`, `maintenance_id`),
    FOREIGN KEY (`robot_id`) REFERENCES `robot`(`robot_id`) ON DELETE CASCADE,
    FOREIGN KEY (`maintenance_id`) REFERENCES `maintenance`(`maintenance_id`) ON DELETE CASCADE
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb3;

-- Вставка зв'язків між роботами та технічним обслуговуванням
INSERT INTO `robot_maintenance` (robot_id, maintenance_id) VALUES (1, 1);  -- Робот 1 проходить техобслуговування 1
INSERT INTO `robot_maintenance` (robot_id, maintenance_id) VALUES (1, 2);  -- Робот 1 проходить техобслуговування 2
INSERT INTO `robot_maintenance` (robot_id, maintenance_id) VALUES (2, 1);  -- Робот 2 проходить техобслуговування 1
INSERT INTO `robot_maintenance` (robot_id, maintenance_id) VALUES (2, 3);  -- Робот 2 проходить техобслуговування 3
INSERT INTO `robot_maintenance` (robot_id, maintenance_id) VALUES (3, 1);  -- Робот 3 проходить техобслуговування 1
INSERT INTO `robot_maintenance` (robot_id, maintenance_id) VALUES (3, 4);  -- Робот 3 проходить техобслуговування 4
INSERT INTO `robot_maintenance` (robot_id, maintenance_id) VALUES (4, 5);  -- Робот 4 проходить техобслуговування 5
INSERT INTO `robot_maintenance` (robot_id, maintenance_id) VALUES (5, 6);  -- Робот 5 проходить техобслуговування 6
INSERT INTO `robot_maintenance` (robot_id, maintenance_id) VALUES (6, 7);  -- Робот 6 проходить техобслуговування 7
INSERT INTO `robot_maintenance` (robot_id, maintenance_id) VALUES (7, 1);  -- Робот 7 проходить техобслуговування 1

-- -----------------------------------------------------
-- Data for table `operator`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `operator` (`operators_id`, `name`, `shift_start`, `shift_end`, `contact_info`) VALUES (1, 'Аліна Коваль', '08:00:00', '16:00:00', 'alina.koval@example.com');
INSERT INTO `operator` (`operators_id`, `name`, `shift_start`, `shift_end`, `contact_info`) VALUES (2, 'Максим Петренко', '16:00:00', '00:00:00', 'maxim.petrenko@example.com');
INSERT INTO `operator` (`operators_id`, `name`, `shift_start`, `shift_end`, `contact_info`) VALUES (3, 'Олександр Сидоренко', '00:00:00', '08:00:00', 'oleksandr.sydorenko@example.com');
INSERT INTO `operator` (`operators_id`, `name`, `shift_start`, `shift_end`, `contact_info`) VALUES (4, 'Ірина Мельник', '08:00:00', '16:00:00', 'iryna.melynok@example.com');
INSERT INTO `operator` (`operators_id`, `name`, `shift_start`, `shift_end`, `contact_info`) VALUES (5, 'Володимир Гнатюк', '16:00:00', '00:00:00', 'volodymyr.hnatyuk@example.com');
INSERT INTO `operator` (`operators_id`, `name`, `shift_start`, `shift_end`, `contact_info`) VALUES (6, 'Софія Ярошенко', '00:00:00', '08:00:00', 'sofia.yaroshenko@example.com');
INSERT INTO `operator` (`operators_id`, `name`, `shift_start`, `shift_end`, `contact_info`) VALUES (7, 'Дмитро Кравченко', '08:00:00', '16:00:00', 'dmytro.kravchenko@example.com');

COMMIT;


-- -----------------------------------------------------
-- Data for table `charging_station`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `charging_station` (`station_id`, `location`, `capacity`, `available`) VALUES (1, 'Station A', 10, 'yes');
INSERT INTO `charging_station` (`station_id`, `location`, `capacity`, `available`) VALUES (2, 'Station B', 15, 'no');
INSERT INTO `charging_station` (`station_id`, `location`, `capacity`, `available`) VALUES (3, 'Station C', 12, 'yes');
INSERT INTO `charging_station` (`station_id`, `location`, `capacity`, `available`) VALUES (4, 'Station D', 8, 'yes');
INSERT INTO `charging_station` (`station_id`, `location`, `capacity`, `available`) VALUES (5, 'Station E', 20, 'no');
INSERT INTO `charging_station` (`station_id`, `location`, `capacity`, `available`) VALUES (6, 'Station F', 5, 'yes');
INSERT INTO `charging_station` (`station_id`, `location`, `capacity`, `available`) VALUES (7, 'Station G', 7, 'yes');

COMMIT;


-- -----------------------------------------------------
-- Data for table `robot`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `robot` (`robot_id`, `status`, `max_distance`, `operator_id`, `station_id`, `alternative_power_source`) VALUES (1, 'Active', 100, 1, 1, 'yes');
INSERT INTO `robot` (`robot_id`, `status`, `max_distance`, `operator_id`, `station_id`, `alternative_power_source`) VALUES (2, 'Inactive', 120, 2, 2, 'no');
INSERT INTO `robot` (`robot_id`, `status`, `max_distance`, `operator_id`, `station_id`, `alternative_power_source`) VALUES (3, 'Maintenance', 150, 3, 3, 'yes');
INSERT INTO `robot` (`robot_id`, `status`, `max_distance`, `operator_id`, `station_id`, `alternative_power_source`) VALUES (4, 'Active', 80, 4, 4, 'no');
INSERT INTO `robot` (`robot_id`, `status`, `max_distance`, `operator_id`, `station_id`, `alternative_power_source`) VALUES (5, 'Inactive', 130, 5, 5, 'yes');
INSERT INTO `robot` (`robot_id`, `status`, `max_distance`, `operator_id`, `station_id`, `alternative_power_source`) VALUES (6, 'Active', 110, 6, 6, 'no');
INSERT INTO `robot` (`robot_id`, `status`, `max_distance`, `operator_id`, `station_id`, `alternative_power_source`) VALUES (7, 'Maintenance', 90, 7, 7, 'yes');
INSERT INTO `robot` (`robot_id`, `status`, `max_distance`, `operator_id`, `station_id`, `alternative_power_source`) VALUES (8, 'Active', 80, 3, 6, 'yes');
INSERT INTO `robot` (`robot_id`, `status`, `max_distance`, `operator_id`, `station_id`, `alternative_power_source`) VALUES (9, 'Active', 80, 1, 7, 'no');

COMMIT;


-- -----------------------------------------------------
-- Data for table `audio_system`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `audio_system` (`audio_system_id`, `has_speaker`, `has_microphone`, `has_panic_button`, `robot_id`) VALUES (1, 'yes', 'yes', 'yes', 1);
INSERT INTO `audio_system` (`audio_system_id`, `has_speaker`, `has_microphone`, `has_panic_button`, `robot_id`) VALUES (2, 'yes', 'no', 'yes', 2);
INSERT INTO `audio_system` (`audio_system_id`, `has_speaker`, `has_microphone`, `has_panic_button`, `robot_id`) VALUES (3, 'no', 'yes', 'no', 3);
INSERT INTO `audio_system` (`audio_system_id`, `has_speaker`, `has_microphone`, `has_panic_button`, `robot_id`) VALUES (4, 'yes', 'yes', 'no', 4);
INSERT INTO `audio_system` (`audio_system_id`, `has_speaker`, `has_microphone`, `has_panic_button`, `robot_id`) VALUES (5, 'no', 'no', 'yes', 5);
INSERT INTO `audio_system` (`audio_system_id`, `has_speaker`, `has_microphone`, `has_panic_button`, `robot_id`) VALUES (6, 'yes', 'no', 'yes', 6);
INSERT INTO `audio_system` (`audio_system_id`, `has_speaker`, `has_microphone`, `has_panic_button`, `robot_id`) VALUES (7, 'no', 'yes', 'no', 7);
INSERT INTO `audio_system` (`audio_system_id`, `has_speaker`, `has_microphone`, `has_panic_button`, `robot_id`) VALUES (8, 'no', 'no', 'yes', 3);
INSERT INTO `audio_system` (`audio_system_id`, `has_speaker`, `has_microphone`, `has_panic_button`, `robot_id`) VALUES (9, 'no', 'yes', 'yes', 2);
INSERT INTO `audio_system` (`audio_system_id`, `has_speaker`, `has_microphone`, `has_panic_button`, `robot_id`) VALUES (10, 'yes', 'yes', 'no', 3);

COMMIT;


-- -----------------------------------------------------
-- Data for table `alert`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `alert` (`alerts_id`, `type`, `timestamp`, `status`, `audio_system_id`) VALUES (1, 'Intrusion Alert', '2024-09-19 14:30:00', 'Active', 3);
INSERT INTO `alert` (`alerts_id`, `type`, `timestamp`, `status`, `audio_system_id`) VALUES (2, 'Sensor Malfunction', '2024-09-18 16:00:00', 'Resolved', 2);
INSERT INTO `alert` (`alerts_id`, `type`, `timestamp`, `status`, `audio_system_id`) VALUES (3, 'Battery Low', '2024-09-17 10:45:00', 'Active', 1);
INSERT INTO `alert` (`alerts_id`, `type`, `timestamp`, `status`, `audio_system_id`) VALUES (4, 'Camera Issue', '2024-09-16 08:00:00', 'Pending', 4);
INSERT INTO `alert` (`alerts_id`, `type`, `timestamp`, `status`, `audio_system_id`) VALUES (5, 'Signal Lost', '2024-09-15 19:30:00', 'Resolved', 5);
INSERT INTO `alert` (`alerts_id`, `type`, `timestamp`, `status`, `audio_system_id`) VALUES (6, 'Obstacle Detected', '2024-09-14 12:00:00', 'Active', 7);
INSERT INTO `alert` (`alerts_id`, `type`, `timestamp`, `status`, `audio_system_id`) VALUES (7, 'Audio System Issue', '2024-09-13 14:15:00', 'Pending', 6);
INSERT INTO `alert` (`alerts_id`, `type`, `timestamp`, `status`, `audio_system_id`) VALUES (8, 'Signal Lost', '2024-09-10 11:15:00', 'Pending', 3);
INSERT INTO `alert` (`alerts_id`, `type`, `timestamp`, `status`, `audio_system_id`) VALUES (9, 'Audio System Issue', '2024-09-13 19:15:00', 'Pending', 7);
INSERT INTO `alert` (`alerts_id`, `type`, `timestamp`, `status`, `audio_system_id`) VALUES (10, 'Sensor Malfunction', '2024-09-13 23:15:00', 'Pending', 3);

COMMIT;


-- -----------------------------------------------------
-- Data for table `battery`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `battery` (`battery_id`, `log_time`, `battery_level`, `robot_id`, `temperature`) VALUES (1, '2024-09-19 08:00:00', 85, 1, '35.5°C');
INSERT INTO `battery` (`battery_id`, `log_time`, `battery_level`, `robot_id`, `temperature`) VALUES (2, '2024-09-18 16:00:00', 40, 2, '37.2°C');
INSERT INTO `battery` (`battery_id`, `log_time`, `battery_level`, `robot_id`, `temperature`) VALUES (3, '2024-09-17 10:00:00', 55, 3, '36.1°C');
INSERT INTO `battery` (`battery_id`, `log_time`, `battery_level`, `robot_id`, `temperature`) VALUES (4, '2024-09-16 12:00:00', 20, 4, '38.0°C');
INSERT INTO `battery` (`battery_id`, `log_time`, `battery_level`, `robot_id`, `temperature`) VALUES (5, '2024-09-15 19:00:00', 70, 5, '34.8°C');
INSERT INTO `battery` (`battery_id`, `log_time`, `battery_level`, `robot_id`, `temperature`) VALUES (6, '2024-09-14 14:00:00', 60, 6, '36.7°C');
INSERT INTO `battery` (`battery_id`, `log_time`, `battery_level`, `robot_id`, `temperature`) VALUES (7, '2024-09-13 09:00:00', 50, 7, '35.9°C');
INSERT INTO `battery` (`battery_id`, `log_time`, `battery_level`, `robot_id`, `temperature`) VALUES (8, '2024-09-13 23:00:00', 15, 3, '38.5°C');
INSERT INTO `battery` (`battery_id`, `log_time`, `battery_level`, `robot_id`, `temperature`) VALUES (9, '2024-09-23 11:00:00', 75, 5, '34.6°C');
INSERT INTO `battery` (`battery_id`, `log_time`, `battery_level`, `robot_id`, `temperature`) VALUES (10, '2024-09-10 19:00:00', 45, 3, '36.4°C');

COMMIT;


-- -----------------------------------------------------
-- Data for table `camera`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `camera` (`camera_id`, `robot_id`, `resolution`, `zoom_level`, `status`, `night_vision`, `panoramic_view`) VALUES (1, 1, '1920x1080', 10, 'Operational', 'yes', 'no');
INSERT INTO `camera` (`camera_id`, `robot_id`, `resolution`, `zoom_level`, `status`, `night_vision`, `panoramic_view`) VALUES (2, 2, '1280x720', 20, 'Inactive', 'no', 'yes');
INSERT INTO `camera` (`camera_id`, `robot_id`, `resolution`, `zoom_level`, `status`, `night_vision`, `panoramic_view`) VALUES (3, 3, '3840x2160', 15, 'Operational', 'yes', 'yes');
INSERT INTO `camera` (`camera_id`, `robot_id`, `resolution`, `zoom_level`, `status`, `night_vision`, `panoramic_view`) VALUES (4, 4, '1920x1080', 8, 'Malfunctioning', 'yes', 'no');
INSERT INTO `camera` (`camera_id`, `robot_id`, `resolution`, `zoom_level`, `status`, `night_vision`, `panoramic_view`) VALUES (5, 5, '1280x720', 12, 'Operational', 'no', 'no');
INSERT INTO `camera` (`camera_id`, `robot_id`, `resolution`, `zoom_level`, `status`, `night_vision`, `panoramic_view`) VALUES (6, 6, '3840x2160', 18, 'Inactive', 'yes', 'yes');
INSERT INTO `camera` (`camera_id`, `robot_id`, `resolution`, `zoom_level`, `status`, `night_vision`, `panoramic_view`) VALUES (7, 7, '1920x1080', 14, 'Operational', 'no', 'yes');
INSERT INTO `camera` (`camera_id`, `robot_id`, `resolution`, `zoom_level`, `status`, `night_vision`, `panoramic_view`) VALUES (8, 5, '1280x1080', 10, 'Operational', 'no', 'yes');

COMMIT;


-- -----------------------------------------------------
-- Data for table `maintenance`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `maintenance` (`maintenance_id`, `maintenance_date`, `description`, `technician_name`, `next_maintenance`) VALUES (1, '2024-09-19 09:00:00', 'Routine check-up', 'Emily Davis', '2024-10-19 09:00:00');
INSERT INTO `maintenance` (`maintenance_id`, `maintenance_date`, `description`, `technician_name`, `next_maintenance`) VALUES (2, '2024-09-18 11:00:00', 'Sensor replacement', 'Michael Johnson', '2024-10-18 11:00:00');
INSERT INTO `maintenance` (`maintenance_id`, `maintenance_date`, `description`, `technician_name`, `next_maintenance`) VALUES (3, '2024-09-17 14:00:00', 'Battery calibration', 'John Smith', '2024-10-17 14:00:00');
INSERT INTO `maintenance` (`maintenance_id`, `maintenance_date`, `description`, `technician_name`, `next_maintenance`) VALUES (4, '2024-09-16 10:00:00', 'Software update', 'Sara Lee', '2024-10-16 10:00:00');
INSERT INTO `maintenance` (`maintenance_id`, `maintenance_date`, `description`, `technician_name`, `next_maintenance`) VALUES (5, '2024-09-15 13:00:00', 'Component replacement', 'Paul Walker', '2024-10-15 13:00:00');
INSERT INTO `maintenance` (`maintenance_id`, `maintenance_date`, `description`, `technician_name`, `next_maintenance`) VALUES (6, '2024-09-14 15:00:00', 'System diagnostic', 'Anna Clark', '2024-10-14 15:00:00');
INSERT INTO `maintenance` (`maintenance_id`, `maintenance_date`, `description`, `technician_name`, `next_maintenance`) VALUES (7, '2024-09-13 16:00:00', 'Routine check-up', 'David Green', '2024-10-13 16:00:00');
INSERT INTO `maintenance` (`maintenance_id`, `maintenance_date`, `description`, `technician_name`, `next_maintenance`) VALUES (8, '2024-09-30 06:00:00', 'Battery calibration', 'John Smith', '2024-10-20 16:00:00');
INSERT INTO `maintenance` (`maintenance_id`, `maintenance_date`, `description`, `technician_name`, `next_maintenance`) VALUES (9, '2024-09-20 09:00:00', 'Software update', 'Sara Lee', '2024-10-10 16:00:00');
INSERT INTO `maintenance` (`maintenance_id`, `maintenance_date`, `description`, `technician_name`, `next_maintenance`) VALUES (10, '2024-09-24 00:00:00', 'Component replacement', 'Paul Walker', '2024-10-03 16:00:00');

COMMIT;


-- -----------------------------------------------------
-- Data for table `patrol_route`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `patrol_route` (`routes_id`, `start_point`, `end_point`, `difficulty_level`, `robot_id`) VALUES (1, 'Point A', 'Point B', 2, 1);
INSERT INTO `patrol_route` (`routes_id`, `start_point`, `end_point`, `difficulty_level`, `robot_id`) VALUES (2, 'Point C', 'Point D', 3, 2);
INSERT INTO `patrol_route` (`routes_id`, `start_point`, `end_point`, `difficulty_level`, `robot_id`) VALUES (3, 'Point E', 'Point F', 1, 3);
INSERT INTO `patrol_route` (`routes_id`, `start_point`, `end_point`, `difficulty_level`, `robot_id`) VALUES (4, 'Point G', 'Point H', 2, 4);
INSERT INTO `patrol_route` (`routes_id`, `start_point`, `end_point`, `difficulty_level`, `robot_id`) VALUES (5, 'Point I', 'Point J', 3, 5);
INSERT INTO `patrol_route` (`routes_id`, `start_point`, `end_point`, `difficulty_level`, `robot_id`) VALUES (6, 'Point K', 'Point L', 2, 6);
INSERT INTO `patrol_route` (`routes_id`, `start_point`, `end_point`, `difficulty_level`, `robot_id`) VALUES (7, 'Point M', 'Point N', 4, 7);
INSERT INTO `patrol_route` (`routes_id`, `start_point`, `end_point`, `difficulty_level`, `robot_id`) VALUES (8, 'Point A', 'Point L', 1, 8);
INSERT INTO `patrol_route` (`routes_id`, `start_point`, `end_point`, `difficulty_level`, `robot_id`) VALUES (9, 'Point C', 'Point J', 2, 3);
INSERT INTO `patrol_route` (`routes_id`, `start_point`, `end_point`, `difficulty_level`, `robot_id`) VALUES (10, 'Point G', 'Point D', 5, 4);
INSERT INTO `patrol_route` (`routes_id`, `start_point`, `end_point`, `difficulty_level`, `robot_id`) VALUES (11, 'Point L', 'Point A', 5, 2);

COMMIT;


-- -----------------------------------------------------
-- Data for table `patrol_report`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `patrol_report` (`report_id`, `start_time`, `end_time`, `observations`, `person_detected`, `routes_id`) VALUES (1, '2024-09-19 08:00:00', '2024-09-19 16:00:00', 'Routine patrol completed', 'yes', 1);
INSERT INTO `patrol_report` (`report_id`, `start_time`, `end_time`, `observations`, `person_detected`, `routes_id`) VALUES (2, '2024-09-18 16:00:00', '2024-09-18 00:00:00', 'Minor issues with sensors', 'no', 3);
INSERT INTO `patrol_report` (`report_id`, `start_time`, `end_time`, `observations`, `person_detected`, `routes_id`) VALUES (3, '2024-09-17 08:00:00', '2024-09-17 16:00:00', 'Battery low at the end', 'no', 5);
INSERT INTO `patrol_report` (`report_id`, `start_time`, `end_time`, `observations`, `person_detected`, `routes_id`) VALUES (4, '2024-09-16 16:00:00', '2024-09-16 00:00:00', 'Intruder detected', 'yes', 4);
INSERT INTO `patrol_report` (`report_id`, `start_time`, `end_time`, `observations`, `person_detected`, `routes_id`) VALUES (5, '2024-09-15 08:00:00', '2024-09-15 16:00:00', 'Routine patrol completed', 'no', 2);
INSERT INTO `patrol_report` (`report_id`, `start_time`, `end_time`, `observations`, `person_detected`, `routes_id`) VALUES (6, '2024-09-14 16:00:00', '2024-09-14 00:00:00', 'Minor camera issue', 'yes', 7);
INSERT INTO `patrol_report` (`report_id`, `start_time`, `end_time`, `observations`, `person_detected`, `routes_id`) VALUES (7, '2024-09-13 08:00:00', '2024-09-13 16:00:00', 'Obstacle detected on route', 'yes', 2);

COMMIT;


-- -----------------------------------------------------
-- Data for table `sensor`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `sensor` (`sensor_id`, `robot_id`, `technology_used`, `detection_range`, `trigger_status`) VALUES (1, 1, 'Infrared', 50, 'Active');
INSERT INTO `sensor` (`sensor_id`, `robot_id`, `technology_used`, `detection_range`, `trigger_status`) VALUES (2, 2, 'Motion', 100, 'Inactive');
INSERT INTO `sensor` (`sensor_id`, `robot_id`, `technology_used`, `detection_range`, `trigger_status`) VALUES (3, 3, 'Thermal', 70, 'Active');
INSERT INTO `sensor` (`sensor_id`, `robot_id`, `technology_used`, `detection_range`, `trigger_status`) VALUES (4, 4, 'Motion', 80, 'Malfunctioning');
INSERT INTO `sensor` (`sensor_id`, `robot_id`, `technology_used`, `detection_range`, `trigger_status`) VALUES (5, 5, 'Infrared', 60, 'Active');
INSERT INTO `sensor` (`sensor_id`, `robot_id`, `technology_used`, `detection_range`, `trigger_status`) VALUES (6, 6, 'Thermal', 90, 'Inactive');
INSERT INTO `sensor` (`sensor_id`, `robot_id`, `technology_used`, `detection_range`, `trigger_status`) VALUES (7, 7, 'Motion', 50, 'Active');

COMMIT;


-- -----------------------------------------------------
-- Data for table `person_identification`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `person_identification` (`identification_id`, `person_name`, `timestamp`, `accuracy`, `sensor_id`, `camera_id`, `report_id`) VALUES (3, 'Michael Johnson', '2024-09-17 10:50:00', 95.80, 3, 3, 4);
INSERT INTO `person_identification` (`identification_id`, `person_name`, `timestamp`, `accuracy`, `sensor_id`, `camera_id`, `report_id`) VALUES (4, 'Sarah Williams', '2024-09-16 08:05:00', 96.30, 1, 1, 1);
INSERT INTO `person_identification` (`identification_id`, `person_name`, `timestamp`, `accuracy`, `sensor_id`, `camera_id`, `report_id`) VALUES (6, 'Emily Davis', '2024-09-14 12:05:00', 93.60, 7, 7, 6);
INSERT INTO `person_identification` (`identification_id`, `person_name`, `timestamp`, `accuracy`, `sensor_id`, `camera_id`, `report_id`) VALUES (7, 'Chris Evans', '2024-09-13 14:20:00', 98.10, 5, 5, 5);

COMMIT;


-- -----------------------------------------------------
-- Data for table `solar_system`
-- -----------------------------------------------------
START TRANSACTION;
USE `robot_db`;
INSERT INTO `solar_system` (`solar_id`, `status`, `power_output`, `technology_used`, `station_id`) VALUES (1, 'Operational', 1500.5, 'Monocrystalline', 2);
INSERT INTO `solar_system` (`solar_id`, `status`, `power_output`, `technology_used`, `station_id`) VALUES (2, 'Inactive', 0, 'Polycrystalline', 3);
INSERT INTO `solar_system` (`solar_id`, `status`, `power_output`, `technology_used`, `station_id`) VALUES (3, 'Operational', 1200, 'Monocrystalline', 1);
INSERT INTO `solar_system` (`solar_id`, `status`, `power_output`, `technology_used`, `station_id`) VALUES (4, 'Operational', 1800.2, 'Thin-Film', 1);
INSERT INTO `solar_system` (`solar_id`, `status`, `power_output`, `technology_used`, `station_id`) VALUES (5, 'Operational', 2000, 'Monocrystalline', 5);
INSERT INTO `solar_system` (`solar_id`, `status`, `power_output`, `technology_used`, `station_id`) VALUES (6, 'Inactive', 0, 'Polycrystalline', 6);
INSERT INTO `solar_system` (`solar_id`, `status`, `power_output`, `technology_used`, `station_id`) VALUES (7, 'Operational', 1600.8, 'Monocrystalline', 4);

COMMIT;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;