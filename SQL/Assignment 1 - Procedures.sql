USE mydb;

DROP PROCEDURE IF EXISTS `1 - Hospital by ID`;
DROP PROCEDURE IF EXISTS `2 - Hospital by Name`;
DROP PROCEDURE IF EXISTS `3 - Candidate By Surname`;
DROP PROCEDURE IF EXISTS `4 - Candidate with Skill from Position`;
DROP PROCEDURE IF EXISTS `5 - Count of Positions Offered`;
DROP PROCEDURE IF EXISTS `6 - Positions requiring Skill`;
DROP PROCEDURE IF EXISTS `7 - Positions requiring Nursing`;
DROP PROCEDURE IF EXISTS `8 - Positions sorted by Hospital`;
DROP PROCEDURE IF EXISTS `9 - Interviews by Date`;
DROP PROCEDURE IF EXISTS `10 - Candidates with Interviews on Date`;
DROP PROCEDURE IF EXISTS `11 - Candidates with multiple Interviews`;

DELIMITER $$

CREATE PROCEDURE `1 - Hospital by ID`(IN targetID INT)
BEGIN

    SELECT * FROM hospital
    WHERE id=targetID;

END $$

CREATE PROCEDURE `2 - Hospital by Name`(IN targetName VARCHAR(255))
BEGIN

    SELECT * FROM hospital
    WHERE name LIKE concat('%', targetName, '%');

END $$

CREATE PROCEDURE `3 - Candidate By Surname`(IN targetSecondName VARCHAR(30))
BEGIN

    SELECT * FROM candidate
    WHERE second_name=targetSecondName;

END $$

CREATE PROCEDURE `4 - Candidate with Skill from Position`(IN targetPositionID INT)
BEGIN

	SELECT candidate.id, first_name, second_name,
    job_name, 
    candidate_skills.skill
    
    FROM candidate
	JOIN candidate_skills ON candidate.id=candidate_id
	JOIN position_required_skills ON candidate_skills.skill = position_required_skills.skill
	JOIN position ON position_required_skills.position_id = position.id
	
    WHERE position.id=targetPositionID
    GROUP BY candidate.id;

END $$

CREATE PROCEDURE `5 - Count of Positions Offered`()
BEGIN

    SELECT count(*) AS positions_offered FROM application
    WHERE position_offered=TRUE;

END $$

CREATE PROCEDURE `6 - Positions requiring Skill`(IN targetSkill VARCHAR(30))
BEGIN

    SELECT DISTINCT position.* FROM position
    JOIN position_required_skills ON position_id = position.id
    WHERE skill = targetSkill;

END $$

CREATE PROCEDURE `7 - Positions requiring Nursing`()
BEGIN

    SELECT DISTINCT position.* FROM position
    JOIN position_required_skills ON position_id = position.id
    WHERE skill = 'Nursing';

END $$

CREATE PROCEDURE `8 - Positions sorted by Hospital`()
BEGIN

    SELECT position.*, hospital.`name` FROM position
    JOIN hospital ON hospital.id = hospital_id
    ORDER BY hospital.`name`;

END $$

CREATE PROCEDURE `9 - Interviews by Date`(IN targetDate DATE)
BEGIN

	SELECT * FROM interview
	WHERE CAST(interview.`datetime` AS DATE) = '2020-10-20';

END $$

CREATE PROCEDURE `10 - Candidates with Interviews on Date`(IN targetDate DATE)
BEGIN
	
    SELECT candidate.id AS candidate_id, first_name, second_name, 
	interview.`datetime` AS interview_datetime
	
    FROM candidate
	JOIN application ON candidate_id = candidate.id
	JOIN interview ON application_id = application.id
	
    WHERE CAST(`datetime` AS DATE) = targetDate
	GROUP BY candidate_id;

END $$

CREATE PROCEDURE `11 - Candidates with multiple Interviews`()
BEGIN
	
    SELECT candidate.id, first_name, second_name 
    
    FROM interview    
    JOIN application ON application.id = application_id
	JOIN candidate ON candidate_id = candidate.id
	
    GROUP BY candidate.id
	HAVING count(interview.id) > 1;

END $$

DELIMITER ;