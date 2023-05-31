-- Users
INSERT INTO "Users"(id, "email", "password", "firstName", "lastName", "is_superuser", 
					"is_staff", "isDeleted", "isVerified", "creationDate", "verificationCode", "role")
VALUES				(1, 'admin@mail.ru', 'pbkdf2_sha256$390000$BkmrquE1FSW9Vl6Z1Z334j$hVVRBLFJ9rFUC40KIVV1UD+AkMsnKfA6jPrkpC6X1CU=', 'Admin', 'Adminovich', true, true, false, true, '20230101 00:00', '1234', 1),
					(2, 'anuar@mail.ru', 'pbkdf2_sha256$390000$BkmrquE1FSW9Vl6Z1Z334j$hVVRBLFJ9rFUC40KIVV1UD+AkMsnKfA6jPrkpC6X1CU=', 'Anuar', 'Bora', false, false, false, true, '20230101 00:00', '1234', 2),
					(3, 'anuarGuide@mail.ru', 'pbkdf2_sha256$390000$BkmrquE1FSW9Vl6Z1Z334j$hVVRBLFJ9rFUC40KIVV1UD+AkMsnKfA6jPrkpC6X1CU=', 'AnuGuide', 'Guidevich', false, false, false, true, '20230101 00:00', '1234', 3),
					(4, 'anuarBusiness@mail.ru', 'pbkdf2_sha256$390000$BkmrquE1FSW9Vl6Z1Z334j$hVVRBLFJ9rFUC40KIVV1UD+AkMsnKfA6jPrkpC6X1CU=', 'Anu', 'BoraBuis', false, false, false, true, '20230101 00:00', '1234', 4),
					(5, 'sultan@mail.ru', 'pbkdf2_sha256$390000$BkmrquE1FSW9Vl6Z1Z334j$hVVRBLFJ9rFUC40KIVV1UD+AkMsnKfA6jPrkpC6X1CU=', 'Sultan', 'Rakhma', false, false, false, true, '20230101 00:00', '1234', 5);

INSERT INTO "Guide"(id, "serviceRating", "user_id")
VALUES	(1, 7.8, 3);

INSERT INTO "BusinessPerson"(id, "companyName", "binNumber", "legalAddress", "serviceRating", "user_id")
VALUES	(1, 'BoraCompany', '181700015139','Almaty, Manasa st.', 8.9, 4);

INSERT INTO "Driver"(id, "yearExperience", "phoneNumber", "user_id")
VALUES	(1, 4, '87079998877', 5);

--Resource Code, Resource Values, Language
INSERT INTO "ResourceCode"(id, "defaultValue")
VALUES	(1,'Russian'),
		(2,'Kazakh'),
		(3,'English'),
		(4,'Almaty'),
		(5,'Taraz'),
		(6,'Shymkent'),
		(7,'Pavlodar'),
		(8,'Oskemen'),
		(9, 'IntercitySchedule'),
		(10, 'TouristSchedule'),
		(11, 'Town'),
		(12, 'TouristPlace');


INSERT INTO "Language"(id,"nativeName","resourcecode_id")
VALUES	(1,'Русский', 1),
		(2,'Қазақ', 2),
		(3,'English', 3);

INSERT INTO "ResourceValue"(id,value,"language_id","code_id")
VALUES		(1,'Русский', 1,1),
			(2,'Орыс',2,1),
			(3,'Russian',3,1),

			(4,'Алматы',1,4),
			(5,'Алматы',2,4),
			(6,'Almaty',3,4),
			(7,'Тараз',1,5),
			(8,'Тараз',2,5),
			(9,'Taraz',3,5),
			(10,'Шымкент',1,6),
			(11,'Шымкент',2,6),
			(12,'Shymkent',3,6),
			(13,'Павлодар',1,7),
			(14,'Павлодар',2,7),
			(15,'Pavlodar',3,7),
			(16,'Усть-Каменогорск',1,8),
			(17,'Өскемен',2,8),
			(18,'Oskemen',3,8),
			(19,'Межгородний сеанс',1,9),
			(20,'Туристический сеанс',1,10),
			(21,'Населенный пункт',1,11),
			(22,'Туристическое место',1,12);

-- Location
INSERT INTO "LocationType"(id, "nameCode_id")
VALUES 		(1, 11),
			(2, 12);

INSERT INTO "Location"(id,"coordinates","nameCode_id", "type_id")
VALUES	(1,'43,2567N, 76,9286E',4, 1),
		(2,'43,2567N, 76,9286E',4, 2),
		(3,'42,9N, 71,3667E',5, 1),
		(4,'42,9N, 71,3667E',5, 2),
		(5,'42,3N, 69,6E',6, 1),
		(6,'42,3N, 69,6E',6, 2),
		(7,'52,2833N, 76,9667E',7, 1),
		(8,'52,2833N, 76,9667E',7, 2),
		(9,'49,9714N, 82,6059E',8, 1),
		(10,'49,9714N, 82,6059E',8, 2);

--Route
INSERT INTO "Route"(id, "source_id", "destination_id")
VALUES	
		-- Almaty
		(1, 1, 3),
		(2, 3, 1),
		(3, 2, 4),
		(4, 4, 2),
		(5, 1, 5),
		(6, 5, 1),
		(7, 2, 6),
		(8, 6, 2),
		(9, 1, 7),
		(10, 7, 1),
		(11, 2, 8),
		(12, 8, 2),
		(13, 1, 9),
		(14, 9, 1),
		(15, 2, 10),
		(16, 10, 2),
		--Taraz
		(17, 3, 5),
		(18, 5, 3),
		(19, 4, 6),
		(20, 6, 4),
		(21, 3, 7),
		(22, 7, 3),
		(23, 4, 8),
		(24, 8, 4),
		(25, 3, 9),
		(26, 9, 3),
		(27, 4, 10),
		(28, 10, 4),
		--Shymkent
		(29, 5, 7),
		(30, 7, 5),
		(31, 6, 8),
		(32, 8, 6),
		(33, 5, 9),
		(34, 9, 5),
		(35, 6, 10),
		(36, 10, 6),
		--Pavlodar
		(37, 7, 9),
		(38, 9, 7),
		(39, 8, 10),
		(40, 10, 8);

-- Bus

INSERT INTO "BusType"(id,name,"capacity", template)
	VALUES(1,'class A',40, '<tr data-bs-toggle="collapse" data-bs-target="#bus3">
    <th scope="row"><span id="schedule-number">AB4958</span></th>
    <td><span id="route-source-dest">Almaty - Taraz</span></td>
    <td><span id="begin-end-date">10:40pm - 05:30pm</span></td>
</tr>
                       
<td colspan="3" class="collapse " id="bus3">
    <div class="row align-items-center " id="bus3">
            <div class="col-md-9 p-2 my-5 bus-seats mx-auto text-center">
                <ul v-for="row in tickets" class="list-group list-group-horizontal">
                    <li v-for="ticket in row" :key="ticket.id" :class="currentStatusColor(ticket.ticketStatus)" @click="occupySeat(ticket)" class="list-group-item availableSeat m-1 mx-2 text-center flex-wrap">
                        <span :id=ticket.id>{{ ticket.seatNumber }}</span>
                    </li>
                </ul>  
            </div>      
            <div class="col-md-3 mx-auto">
                    <h6 class="mb-3 py-3 colour mx-auto availableSeat">Available</h6>
                    <h6 class="mb-3 py-3 colour mx-auto occupiedSeat">Occupied</h6>
                    <h6 class="mb-3 py-3 colour mx-auto bookedSeat">Booked</h6>
                    <button type="button" class="btn btn-primary mx-auto my-3">Buy</button>
            </div>        
    </div>
</td>'),
(2,'class B',40, '<tr data-bs-toggle="collapse" data-bs-target="#bus3">
    <th scope="row"><span id="schedule-number">AB4958</span></th>
    <td><span id="route-source-dest">Almaty - Taraz</span></td>
    <td><span id="begin-end-date">10:40pm - 05:30pm</span></td>
</tr>
                       
<td colspan="3" class="collapse " id="bus3">
    <div class="row align-items-center " id="bus3">
            <div class="col-md-9 p-2 my-5 bus-seats mx-auto text-center">
                <ul v-for="row in tickets" class="list-group list-group-horizontal">
                    <li v-for="ticket in row" :key="ticket.id" :class="currentStatusColor(ticket.ticketStatus)" @click="occupySeat(ticket)" class="list-group-item availableSeat m-1 mx-2 text-center flex-wrap">
                        <span :id=ticket.id>{{ ticket.seatNumber }}</span>
                    </li>
                </ul>  
            </div>      
            <div class="col-md-3 mx-auto">
                    <h6 class="mb-3 py-3 colour mx-auto availableSeat">Available</h6>
                    <h6 class="mb-3 py-3 colour mx-auto occupiedSeat">Occupied</h6>
                    <h6 class="mb-3 py-3 colour mx-auto bookedSeat">Booked</h6>
                    <button type="button" class="btn btn-primary mx-auto my-3">Buy</button>
            </div>        
    </div>
</td>');

	INSERT INTO "Bus"(id,name,"type_id")
	VALUES	(1, 'Mercedes', 1),
			(2, 'Toyota', 2),
			(3, 'BMW', 1);
--Schedule
INSERT INTO "ScheduleType"(id, "nameCode_id")
VALUES	(1, 9), 
		(2, 10);

INSERT INTO "Schedule" (id, "scheduleNumber", "beginDate", "endDate", "weekDay", "isActive",
					   	"driver_id", "bus_id", "route_id", "scheduleType_id", "creationDate")

VALUES					--Intercity schedules
						(1, 'AB4958', '2023/06/02 14:00:00', '2023/06/03 12:00:00', 5, true, 5, 1, 1, 1, '20230601'),
						(2, 'BX2551', '2023/06/03 17:00:00', '2023/06/04 05:00:00', 6, true, 5, 1, 3, 1, '20230601'),
						(3, 'LN1266', '2023/06/05 09:30:00', '2023/06/07 10:15:00', 1, true, 5, 2, 5, 1, '20230601');

-- Ticket
INSERT INTO "TicketStatus"(id,name) 
VALUES		(1,'Occupied'),
		  	(2,'Booked'),
		  	(3,'Available');

INSERT INTO "TicketType"(id,"name")
VALUES	(1, 'Bus'),
		(2, 'Tour');

-- Insert Tickets for intercity schedules
do 
$$

DECLARE 
	schedule_cursor cursor for select *
				from "Schedule"
				where "scheduleType_id" = 1;
	schedule "Schedule"%ROWTYPE;
BEGIN
	open schedule_cursor;
	
	loop
		fetch next from schedule_cursor into schedule;
		exit when not found;
		raise notice 'Current schedule id: %', schedule.id;
		
		for counter in 1..40 loop
			INSERT INTO "Ticket" ("seatNumber", "cost", "schedule_id", "status_id", "type_id", "creationDate")
			VALUES	(counter, 4000, schedule.id, 3, 1, '2023/06/01');
		end loop;
		
	end loop;
	close schedule_cursor;
				
END;
$$;

-- PassportNumberTypes
INSERT INTO "PassportNumberType"(id, "typeName", format)
VALUES	(1,'identification','[0-9]{9}'),
		(2,'kz_passport','^([A-Z]{1})([0-9]{8})');

-- Documents

INSERT INTO "DocumentsType"(id, "name", "creationDate") -- gotta define with Sultan
VALUES	(1, 'CV/Resume', '2023/05/22'),
		(2, 'Drivers licence', '2023/05/22'),
		(3, 'Tech Passport', '2023/05/22'),
		(4, 'Identification', '2023/05/22');


--Aplication
INSERT INTO "ApplicationStatus"
VALUES	(1, 'Pending'),
		(2, 'Approved'),
		(3, 'Rejected');

INSERT INTO "ApplicationType"(id, "name")
VALUES	(1, 'HireGuide'),
		(2, 'FireGuide'),
		(3, 'Sabbatical'),
		(4, 'New Route'),
		(5, 'Remove Route');
