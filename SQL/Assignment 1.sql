
/* Clear the database */
DROP DATABASE IF EXISTS cosson16498802;
CREATE DATABASE cosson16498802;
USE cosson16498802;

/*

	Create Tables

*/

CREATE TABLE address (
	id int AUTO_INCREMENT,
    line1 varchar(45) NOT NULL,
    line2 varchar(45),
    city varchar(30) NOT NULL,
    country varchar(30) NOT NULL,
    postal_code varchar(15),
    PRIMARY KEY(id)
);

CREATE TABLE hospital (
	id int AUTO_INCREMENT,
    name varchar(45),
    phone_number varchar(15),
    address_id int,
    PRIMARY KEY(id),
    FOREIGN KEY(address_id) REFERENCES address(id)
);

CREATE TABLE `position` (
	id int AUTO_INCREMENT,
    job_name varchar(45) NOT NULL,
    hospital_id int,
    PRIMARY KEY(id),
    FOREIGN KEY(hospital_id) REFERENCES hospital(id)
);

CREATE TABLE position_required_skills (
	position_id int,
    skill varchar(30),
    PRIMARY KEY(position_id, skill),
    FOREIGN KEY(position_id) REFERENCES `position`(id)
);

CREATE TABLE candidate (
	id int AUTO_INCREMENT,
    first_name varchar(30) NOT NULL,
    second_name varchar(30),
    phone_number varchar(15),
    address_id int,
    PRIMARY KEY(id),
    FOREIGN KEY(address_id) REFERENCES address(id)
);

CREATE TABLE candidate_skills (
	candidate_id int,
    skill varchar(30),
	PRIMARY KEY(candidate_id, skill),
    FOREIGN KEY(candidate_id) REFERENCES candidate(id)
);

CREATE TABLE application (
	id int AUTO_INCREMENT,
	candidate_id int,
    position_id int,
    position_offered bool NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (candidate_id, position_id),
    FOREIGN KEY (candidate_id) REFERENCES candidate(id),
    FOREIGN KEY (position_id) REFERENCES `position`(id)
);

CREATE TABLE interview (
	id int AUTO_INCREMENT,
    application_id int,
    date date,
    PRIMARY KEY(id),
    FOREIGN KEY (application_id) REFERENCES application(id)
);

/*

	Insert Test Data

		- 10 hospitals
        
		- 23 positions open (0-4 per hospital)
		
        - 40 skills required (1-4 per position)
        
        - 15 candidates
        
        - 36 candidate skills (1-4 per candidate)
        
        - 22 applications (1-3 per candidate)

*/

/* 25 addresses - 10 for the 10 hospitals, and 15 for the 15 candidates */
INSERT INTO address(id, line1, line2, city, country, postal_code)
VALUES
(1, 'P.O. Box 1297', 'Beaumont Road', 'Dublin 9', 'Ireland', 'D09 V2N0'),
(2, 'Coombe hospital', 'Dolphin\'s Barn Street', 'Dublin 8', 'Ireland', 'D08 XW7X'),
(3, 'Mater Misericordiae University Hospital', 'Eccles St', 'Dublin 7', 'Ireland', 'D07 K201'),
(4, 'National Maternity Hospital', 'Holles Street', 'Dublin 2', 'Ireland', 'D02 YH21'),
(5, 'Our Lady\'s Childrens Hospital', 'Crumlin', 'Dublin 12', 'Ireland', 'D12 N512'),
(6, 'Rotunda Hospital', 'Parnell Street', 'Dublin 1', 'Ireland', 'D01 P5W9'),
(7, 'Royal Victoria Eye & Ear Hospital', 'Adelaide Road', 'Dublin 2', 'Ireland', 'D02 XK51'),
(8, 'St James Hospital', 'James Street', 'Dublin 8', 'Ireland', 'D08 NHY1'),
(9, 'St Vincent\'s Hospital', 'Convent Avenue', 'Dublin 3', 'Ireland', 'D03 XK40'),
(10, 'Beacon Hospital, Beacon Court', 'Sandyford Business Park', 'Dublin 18', 'Ireland', 'D18 AK68'),
(11, '34 Moyglass Grove', null, 'Lucan', 'Ireland', 'K78 YX98'),
(12, '8 Bridgewater Mews', 'Linenhall St', 'Dundalk', 'Ireland', 'A91 NCD0'),
(13, 'sea front rd', null, 'Bray', 'Ireland', null),
(14, '4 Sandwich Street', 'Dublin 2', 'Dublin', 'Ireland', 'D02 XP65'),
(15, 'Airside Bus. Pk.', null, 'Swords', 'Ireland', 'K67 V654'),
(16, '9 Main st', 'Rathanagan', 'Kildare', 'Ireland', 'R51 VX90'),
(17, '15 Castlewood tce', null, 'Dublin', 'Ireland', 'D06 E2C3'),
(18, '28 South William Street', 'Dublin 2', 'Dublin', 'Ireland', 'D02 W1W9'),
(19, '143 Lr Drumcondra Rd', 'Dublin 9', 'Dublin', 'Ireland', 'D09 R9C3'),
(20, '19 Priory Hall', 'Dublin 12', 'Dublin', 'Ireland', 'D12 FY63'),
(21, 'Shannon Airport', null, 'Shannon', 'Ireland', 'V14 TF44'),
(22, 'Castle Village', 'Celbridge', 'Maynooth', 'Ireland', 'W23 N8W3'),
(23, '2 Anglesea la', 'Dun Laoghaire', 'Dublin', 'Ireland', null),
(24, 'Apartment 1', '9 Kickham street', 'Carrick-on-suir', 'Ireland', 'E32 R990'),
(25, 'Knocknagarn', 'Glenageary Heights', 'Glenageary', 'Ireland', null);

INSERT INTO hospital(id, name, phone_number, address_id)
VALUES 
(1, 'Beaumont', null, 1),
(2, 'Coombe', '01 4085485', 2),
(3, 'Mater Misericordiae', null, 3),
(4, 'National Maternity Hospital', '353 1 637 3100', 4),
(5, 'Our Lady\'s Childrens Hospital', null, 5),
(6, 'Rotunda', '01 817 1700', 6),
(7, 'Royal Victoria Eye & Ear Hospital', null, 7),
(8, 'St James Hospital', '410 3000', 8),
(9, 'St Vincent\'s Hospital', '353 1 8842498', 9),
(10, 'Beacon Hospital', '01 293 6600', 10);

INSERT INTO `position`(id, job_name, hospital_id)
VALUES
(1, 'Senior Occupational Therapist', 1),
(2, 'Staff Nurse', 1),
(3, 'Senior Speech and Language Therapist', 1),
(4, 'Carpenter - Internal maintenance builder', 2),
(5, 'Clinical Midwife Manager 1', 2),
(6, 'Clinical Midwife Specialist - Ultrasound', 2),
(7, 'Staff Nursing - Radiology', 3),
(8, 'Staff Nursing - Operating Theatre', 3),
(9, 'Head of Internal Audit', 5),
(10, 'Clinical Nurse Manager', 5),
(11, 'Clinical Nurse Specialist - Childrens pain', 5),
(12, 'Registrar in Anaesthesia', 6),
(13, 'Ophthalmic Physician - Medical Retina', 7),
(14, 'Registrar in Anaesthesiology', 7),
(15, 'Registrar in Otolaryngology', 7),
(16, 'Clinical Nurse Specialist - Heart Support', 8),
(17, 'Porter', 8),
(18, 'Clinical Nurse Specialist - Hepatology', 8),
(19, 'Staff Nurse', 9),
(20, 'Graduate Nurse', 9),
(21, 'Kitchen Portering', 10),
(22, 'IT Data Analyst', 10),
(23, 'Staff Nurse - Oncology Day Unit', 10);

INSERT INTO position_required_skills(position_id, skill)
VALUES
(1, 'Therapy'),
(1, 'Leadership'),
(1, 'Research'),
(1, 'Planning'),
(2, 'Nursing'),
(3, 'Speech Therapy'),
(3, 'Leadership'),
(4, 'Carpentry'),
(4, 'Maintenance'),
(5, 'Midwifery'),
(5, 'Leadership'),
(6, 'Midwifery'),
(6, 'Radiography'),
(7, 'Nursing'),
(7, 'Radiology'),
(8, 'Nursing'),
(9, 'Accountancy'),
(9, 'Leadership'),
(10, 'Midwifery'),
(10, 'Nursing'),
(10, 'Leadership'),
(11, 'Nursing'),
(11, 'Pain Management'),
(12, 'Anaesthesiology'),
(13, 'Ophthalmology'),
(14, 'Anaesthesiology'),
(15, 'Otolaryngology'),
(16, 'Nursing'),
(16, 'Heart Support'),
(17, 'Customer Service'),
(18, 'Nursing'),
(18, 'Hepatology'),
(19, 'Nursing'),
(20, 'Nursing'),
(21, 'Customer Service'),
(22, 'Numerical Analysis'),
(22, 'Communication'),
(23, 'Nursing'),
(23, 'Midwifery'),
(23, 'Oncology');

INSERT INTO candidate (id, first_name, second_name, phone_number, address_id)
VALUES
(1,	'Kerry', 'Kelly', '123 1111', 11),
(2,	'Carson', 'Moore', '123 1112', 12),
(3,	'Belle', 'Magginson', '123 1113', 13),
(4,	'Catherine', 'Conolly', '123 1114', 14),
(5,	'George', 'Sermon', '123 1115', 15),
(6,	'David', 'Callone', '123 1116', 16),
(7,	'Molly', 'Ni Callaigh', '123 1117', 17),
(8,	'Harry', 'Iverson', '123 1118', 18),
(9,	'Susan', 'Door', '123 1119', 19),
(10,'Leah', 'Buckinson', '123 1121', 20),
(11,'Dylan', 'Kierans', '123 1121', 20),
(12,'Francis', 'Lambridge', '123 1131', 21),
(13,'John', 'Kelly', '123 1141', 22),
(14,'Claire', 'Tomkin', '123 1151', 23),
(15,'Lars', null, '123 1161', 24);

INSERT INTO candidate_skills(candidate_id, skill)
VALUES
(1, 'Therapy'),
(1, 'Leadership'),
(1, 'Research'),
(1, 'Planning'),
(2, 'Speech Therapy'),
(2, 'Leadership'),
(3, 'Carpentry'),
(3, 'Maintenance'),
(4, 'Midwifery'),
(4, 'Radiography'),
(4, 'Nursing'),
(5, 'Accountancy'),
(5, 'Leadership'),
(6, 'Midwifery'),
(6, 'Nursing'),
(6, 'Leadership'),
(7, 'Nursing'),
(7, 'Pain Management'),
(8, 'Anaesthesiology'),
(9, 'Ophthalmology'),
(10, 'Otolaryngology'),
(11, 'Numerical Analysis'),
(11, 'Communication'),
(12, 'Oncology'),
(12, 'Nursing'),
(12, 'Midwifery'),
(13, 'Nursing'),
(13, 'Heart Support'),
(13, 'Leadership'),
(14, 'Nursing'),
(14, 'Therapy'),
(14, 'Leadership'),
(14, 'Research'),
(14, 'Planning'),
(15, 'Nursing'),
(15, 'Hepatology');

INSERT INTO application(id, candidate_id, position_id, position_offered)
VALUES
(1, 1, 1, TRUE),
(2, 2, 3, FALSE),
(3, 3, 4, TRUE),
(4, 4, 6, FALSE),
(5, 4, 8, FALSE),
(6, 5, 9, FALSE),
(7, 6, 2, FALSE),
(8, 6, 8, FALSE),
(9, 6, 10, FALSE),
(10, 7, 11, TRUE),
(11, 8, 12, FALSE),
(12, 8, 14, FALSE),
(13, 9, 13, FALSE),
(14, 10, 15, TRUE),
(15, 11, 22, TRUE),
(16, 12, 23, FALSE),
(17, 13, 19, FALSE),
(18, 13, 20, TRUE),
(19, 14, 1, FALSE),
(20, 14, 2, FALSE),
(21, 14, 19, FALSE),
(22, 15, 18, FALSE);
