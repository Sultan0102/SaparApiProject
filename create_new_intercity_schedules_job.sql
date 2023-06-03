DROP TABLE IF EXISTS temp_schedule_ids;

CREATE TEMP TABLE temp_schedule_ids(
	id integer
);

INSERT INTO temp_schedule_ids
SELECT id FROM "Schedule" s
WHERE s."beginDate"::date = CURRENT_DATE::date
AND s."weekDay" = EXTRACT(dow from CURRENT_DATE::date)
AND "scheduleType_id" = 1
AND "isActive" = true;


INSERT INTO "Schedule"("scheduleNumber", "weekDay", "beginDate", "endDate", "route_id", "scheduleType_id", "isActive", "creationDate")
SELECT (random_character(2) || random_integer_str(4))
		, s."weekDay"
		, s."beginDate" + Interval '7 day'
		, s."endDate" + Interval '7 day'
		, s."route_id"
		, s."scheduleType_id"
		, false
		, CURRENT_DATE
FROM "Schedule" s 
WHERE s.id IN (SELECT id FROM temp_schedule_ids);