DROP TABLE IF EXISTS temp_schedule_ids;

CREATE TEMP TABLE temp_schedule_ids(
	id integer
);

INSERT INTO temp_schedule_ids
SELECT id FROM "Schedule" 
WHERE "scheduleType_id" = 1
AND "endDate"::date < CURRENT_DATE::date;

UPDATE "Schedule"
SET "deleteDate" = CURRENT_DATE 
WHERE ID in (select id from temp_schedule_ids);