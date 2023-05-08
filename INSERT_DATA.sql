insert into Roles(roleName)
values
(1, 'Admin'),
(2, 'Customer'),
(3, 'Guide'),
(4, 'BusinessPerson');

INSERT INTO "Users"(id, "email", "password", "firstName", "lastName", "is_superuser", "is_staff", "isDeleted", "isVerified", "creationDate", "verificationCode")
	VALUES(1, 'anuar@mail.ru', 'anuar123', 'Anuar', 'Bora', true, true, false, true, '20230101 00:00', '123');



	INSERT INTO "TicketStatus"(id,name) 
	VALUES(1,'Occupied'),
		  (2,'Booked'),
		  (3,'Available');

	INSERT INTO "PassportNumberType"(id, "typeName", format)
	VALUES(1,'identification','[0-9]{9}'),
		  (2,'kz_passport','^([A-Z]{1})([0-9]{8})');

	INSERT INTO "ResourceCode"(id, "defaultValue")
	VALUES(1,'Russian'),
		  (2,'Kazakh'),
		  (3,'English'),
		  (4,'Almaty'),
		  (5,'Taraz'),
		  (6,'Shymkent'),
		  (7,'Pavlodar'),
		  (8,'Oskemen'),
		  (9,'Kolsai Lake'),
		  (10,'Kolsai lakes - located in the northern Tien Shan on the territory of the State National Natural Park "Kolsai Koldery", 
		   at a distance of about 280 km from Almaty, they are located at an altitude of 1818 m, 2252 and 2850 m above sea level, respectively.
		   The total zone of the protected regime is 778.8 thousand hectares. The nature around the lake fascinates at first sight.'),
		  (11,'Kayindy Lake'),
		  (12,'The Almaty region is known for its picturesque places and one of them is the enchanting lake of incredible beauty - Kaiyndy.
		  It belongs to the "Kolsai Lakes" system and is its brightest representative. The pond is surrounded by tall fir trees, but its name means
		  “full of birches”, despite the fact that birch groves are located a few kilometers from Kaiynda.'),
		  (13,'Big Almaty Lake'),
		  (14,'Every Almaty resident and guest of our city is obliged to visit BAO. How can one get to know Almaty without knowing the beauty of the surrounding mountains? That is right - no way.
		       Big Almaty Lake, like Medeu, is located in close proximity to the city center. It is located at an altitude of 2510 meters, which is higher
		       dam Medeu at 750 meters.'),
          (15, 'IntercitySchedule'),
          (16, 'TouristSchedule'),
		  (17, 'Town'),
		  (18, 'TouristPlace');

	INSERT INTO "Language"(id,"nativeName","resourcecode_id")
	VALUES(1,'Русский',1),
		  (2,'Қазақ',2),
		  (3,'English',3);

	INSERT INTO "ResourceValue"(id,value,"language_id","nameCode_id")
	VALUES(1,'Русский',1,1),
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
		  (19,'Межгородний сеанс',1,15),
		  (20,'Туристический сеанс',1,16);

	INSERT INTO "LocationType"(id, "nameCode_id")
	VALUES (1, 17),
		   (2, 18);

	INSERT INTO "Location"(id,"coordinates","nameCode_id", "locationType_id")
	VALUES(1,'43,2567N, 76,9286E',4, 1),
		  (2,'42,9N, 71,3667E',5, 1),
		  (3,'42,3N, 69,6E',6, 1),
		  (4,'52,2833N, 76,9667E',7, 1),
		  (5,'49,9714N, 82,6059E',8, 1);

	INSERT INTO "Route"(id,"duration","distance","destination_id","source_id")
	VALUES(1,'03:00','490',1,2),
		  (2,'26:00','1709',3,4),
		  (3,'03:00','490',2,1),
		  (4,'12:00','800',2,5);

	INSERT INTO "TicketType"(id,"name")
	VALUES(1, 'Bus'),
		  (2, 'Tour');

	-- Tickets for schedule with ID = 1
	INSERT INTO "Ticket"(id, "cost", "seatNumber", "schedule_id", "type_id", "status_id", "creationDate")
	VALUES  (1, 3000, 1, 1, 1, 3, '20230116'),
			(2, 3000, 2, 1, 1, 3, '20230116'),
			(3, 3000, 3, 1, 1, 3, '20230116'),
			(4, 3000, 4, 1, 1, 3, '20230116'),(5, 3000, 5, 1, 1, 3, '20230116'),(6, 3000, 6, 1, 1, 3, '20230116'),(7, 3000, 7, 1, 1, 3, '20230116'),(8, 3000, 8, 1, 1, 3, '20230116'),(9, 3000, 9, 1, 1, 3, '20230116'),
			(10, 3000, 10, 1, 1, 3, '20230116'),(11, 3000, 11, 1, 1, 3, '20230116'),(12, 3000, 12, 1, 1, 3, '20230116'),(13, 3000, 13, 1, 1, 3, '20230116'),(14, 3000, 14, 1, 1, 3, '20230116'),
			(15, 3000, 15, 1, 1, 3, '20230116'),(16, 3000, 16, 1, 1, 3, '20230116'),(17, 3000, 17, 1, 1, 3, '20230116'),(18, 3000, 18, 1, 1, 3, '20230116'),(19, 3000, 19, 1, 1, 3, '20230116'),
			(20, 3000, 20, 1, 1, 3, '20230116'),(21, 3000, 21, 1, 1, 3, '20230116'),(22, 3000, 22, 1, 1, 3, '20230116'),(23, 3000, 23, 1, 1, 3, '20230116'),(24, 3000, 24, 1, 1, 3, '20230116'),(25, 3000, 25, 1, 1, 3, '20230116'),
			(26, 3000, 26, 1, 1, 3, '20230116'),(27, 3000, 27, 1, 1, 3, '20230116'),(28, 3000, 28, 1, 1, 3, '20230116'),(29, 3000, 29, 1, 1, 3, '20230116'),(30, 3000, 30, 1, 1, 3, '20230116'),
			(31, 3000, 31, 1, 1, 3, '20230116'),(32, 3000, 32, 1, 1, 3, '20230116'),(33, 3000, 33, 1, 1, 3, '20230116'),(34, 3000, 34, 1, 1, 3, '20230116'),(35, 3000, 35, 1, 1, 3, '20230116'),
			(36, 3000, 36, 1, 1, 3, '20230116'),(37, 3000, 37, 1, 1, 3, '20230116'),(38, 3000, 38, 1, 1, 3, '20230116'),(39, 3000, 39, 1, 1, 3, '20230116'),(40, 3000, 40, 1, 1, 3, '20230116');

	INSERT INTO "BusType"(id,name,"capacity", template)
	VALUES(1,'class A',52, '<tr data-bs-toggle="collapse" data-bs-target="#bus3">
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
VALUES(1, 'Mercedes', 1),
		(2, 'Toyota', 1),
		(3, 'BMW', 1);

INSERT INTO "ScheduleType"(id, "nameCode_id")
VALUES(1, 15), (2, 16);

INSERT INTO "Schedule"(id,"route_id","bus_id","driver_id","scheduleNumber",
						"creationDate","weekDay","beginDate","endDate",
						"isActive","deleteDate","scheduleType")
VALUES(1,1,1,1,'AB4958','2023-01-16',1,TIMESTAMP'2023-01-16 22:20', 
	TIMESTAMP'2023-01-17 01:20',true,null,1),
		(2,2,2,2,'BX2551','2023-02-15',3,TIMESTAMP'2023-02-09 10:30',
	TIMESTAMP'2023-02-10 12:30:',true,null,1),
		(3,3,3,3,'GH1212','2023-02-16',5,TIMESTAMP'2023-02-25 12:00:00',
		TIMESTAMP'2023-02-26 00:00',true,null,2);

    
INSERT INTO "ApplicationType"(id, "name")
VALUES	(1, 'HireGuide'),
		(2, 'FireGuide');


INSERT INTO "ApplicationStatus"
VALUES	(1, 'Pending'),
		(2, 'Approved'),
		(3, 'Rejected');
	-- INSERT INTO "TouristTrip"(id,"titleNameCode_id","descriptionNameCode_id","owner_id","price","deletedDate","guide_id","schedule_id")
	-- VALUES(1,9,10,1,12000,null,3,1),
	--       (2,11,12,1,10000,null,3,1),
	--       (3,13,14,1,9000,null,3,2);
-- 	INSERT INTO "Order"(id,user_id,"schedule_id",,"totalPrice")
-- 	VALUES(1,1,1,1,5000),
-- 	      (2,2,2,3,7000),
-- 	      (3,1,3,3,5000);