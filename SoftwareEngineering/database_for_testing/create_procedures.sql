# DEPRECATED
## Station Updates / Latest
# Get the latest retrieved dynamic information for each station.

DELIMITER $$
DROP PROCEDURE IF EXISTS stations_latest $$
CREATE PROCEDURE stations_latest()
BEGIN

# Find the latest update time.
SET @max=(SELECT max(retrieved) FROM station_update);

# Get all records corresponding to that latest update.
SELECT * FROM stations
INNER JOIN station_update USING (`number`)
WHERE retrieved=@max;

END$$
DELIMITER ;

