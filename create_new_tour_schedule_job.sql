do 
$$

DECLARE 
	tour_cursor refcursor;
	current_tour "TouristTour"%ROWTYPE;
	schedule "Schedule"%ROWTYPE;
	schedule_id "Schedule".id%TYPE;
	random_schedule_number text;
BEGIN
	open tour_cursor for select *
				from "TouristTour"
				where "deletedDate" is null;
	
	loop
		
		fetch next from tour_cursor into current_tour;
		exit when not found;
		raise notice 'Current tour id: %', current_tour.id;
		
		IF EXISTS(SELECT 1 
				  FROM "Schedule" s
				  INNER JOIN "TourSchedules" ts on s.id = ts."schedule_id" and ts."touristtour_id" = current_tour.id
				  WHERE s."beginDate"::date = CURRENT_DATE::date
				  AND s."weekDay" = EXTRACT(dow from CURRENT_DATE::date)
				 ) 
			AND
			NOT EXISTS(SELECT 1 FROM "Schedule" s
				  INNER JOIN "TourSchedules" ts on s.id = ts."schedule_id" and ts."touristtour_id" = current_tour.id
				  WHERE s."beginDate"::date > CURRENT_DATE::date
				  AND s."weekDay" = EXTRACT(dow from CURRENT_DATE::date)
				  ) --current_date::date, "2023-04-21") = 0
				   
				 THEN
					raise notice 'Create Schedule';
					random_schedule_number := random_character(2) || random_integer_str(4);
					
					-- current day schedule for this tour
					SELECT * INTO schedule FROM "Schedule" s
				  	INNER JOIN "TourSchedules" ts on s.id = ts."schedule_id" and ts."touristtour_id" = current_tour.id
				  	WHERE s."beginDate"::date = CURRENT_DATE::date
				  	AND s."weekDay" = EXTRACT(dow from CURRENT_DATE::date);
					
					-- create Schedule for next week
					INSERT INTO "Schedule"("scheduleNumber", "weekDay", "beginDate", "endDate", "route_id", "scheduleType_id", "isActive", "creationDate")
					VALUES(random_schedule_number 
						   , schedule."weekDay"
						   , schedule."beginDate" + Interval '7 day' 
						   , schedule."endDate" + Interval '7 day'
						   , schedule."route_id"
						   , schedule."scheduleType_id"
						   , false
						   , CURRENT_DATE
						  ) RETURNING id INTO schedule_id;
					
					INSERT INTO "TourSchedules"("schedule_id", "touristtour_id")
					VALUES(schedule_id, current_tour.id);
-- 					raise notice 'Schedule: ID: %, ScheduleNumber: %, BeginDate: %', schedule.id, schedule."scheduleNumber", schedule."beginDate";
					
				 
		END IF;
	end loop;
	close tour_cursor;
	raise notice 'Finished';
	
END;
$$;