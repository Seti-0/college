USE mydb;

DROP PROCEDURE IF EXISTS `New Address`;
DROP PROCEDURE IF EXISTS `New Application`;
DROP PROCEDURE IF EXISTS `New Candidate`;
DROP PROCEDURE IF EXISTS `New Candidate Skill`;
DROP PROCEDURE IF EXISTS `New Hospital`;
DROP PROCEDURE IF EXISTS `New Interview`;
DROP PROCEDURE IF EXISTS `New Position`;
DROP PROCEDURE IF EXISTS `New Position Required Skill`;address

DELIMITER $$

CREATE PROCEDURE `New Address`(
	IN line1 VARCHAR(45), 
    IN line2 VARCHAR(45),
    IN city VARCHAR(30),
    IN country VARCHAR(30),
    IN postal_code VARCHAR(15)
)
BEGIN

    INSERT INTO address(line1, line2, city, country, postal_code)
    VALUES(line1, line2, city, country, postal_code);

END $$

CREATE PROCEDURE `New Application`(	
	IN candidate_id INT, 
    IN position_id INT
)
BEGIN

    INSERT INTO application(candidate_id, position_id)
    VALUES(candidate_id, position_id);

END $$


CREATE PROCEDURE `New Candidate`(
	IN first_name VARCHAR(30),
    IN second_name VARCHAR(30),
    IN phone_number VARCHAR(15),
    IN email_address VARCHAR(60),
    IN address_id INT
)
BEGIN

    INSERT INTO candidate(first_name, second_name, phone_number, email_address, address_id)
    VALUES(first_name, second_name, phone_number, email_address, address_id);

END $$

CREATE PROCEDURE `New Candidate Skill`(
	IN candidate_id INT,
    IN skill VARCHAR(30)
)
BEGIN

    INSERT INTO candidate_skills(candidate_id, skill)
    VALUES(candidate_id, skill);

END $$

CREATE PROCEDURE `New Hospital`(
	IN `name` VARCHAR(45),
    IN phone_number VARCHAR(15),
	IN email_address VARCHAR(60),
    IN address_id INT
)
BEGIN

    INSERT INTO hospital(`name`, phone_number, email_address, address_id)
    VALUES(`name`, phone_number, email_address, address_id);

END $$

CREATE PROCEDURE `New Interview`(
	IN application_id INT,
    IN `datetime` DATETIME
)
BEGIN

    INSERT INTO interview(application_id, `datetime`)
    VALUES(application_id, `datetime`);

END $$

CREATE PROCEDURE `New Position`(
	IN job_name VARCHAR(45),
    IN hospital_id INT
)
BEGIN

    INSERT INTO `position`(job_name, hospital_id)
    VALUES(job_name, hospital_id);

END $$

CREATE PROCEDURE `New Position Required Skill`(
	IN position_id INT,
    IN skill VARCHAR(30)
)
BEGIN

    INSERT INTO position_required_skills(position_id, skill)
    VALUES(position_id, skill);

END $$

DELIMITER ;