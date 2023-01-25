
create table Roles(
	id serial primary key,
	roleName varchar(200)
);

create table Users(
	id serial primary key,
	email varchar,
	password varchar,
	firstName varchar,
	lastName varchar,
	birthDate date,
	isDeleted bool,
	roleId int references Roles(id)
);

create table Documents(
	id serial primary key,
	ownerId int references Users(id),
	file bytea,
	creationDate timestamp,
	deleteDate timestamp
);

create table ApplicationStatus (
	id serial primary key,
	name varchar,
	creationDate timestamp
);

create table Application (
	id serial primary key,
	driverId int references Users(id),
	creationDate timestamp,
	applicationStatus int references ApplicationStatus(id)
);

create table ApplicationDocuments(
	id serial primary key,
	documentId int references Documents(id),
	applicationId int references Application(id)
);

create table ResourceCode(
	id serial primary key,
	defaultValue varchar
);

create table Languages(
	id serial primary key,
	nameCodeId int references ResourceCode(id),
	nativeName varchar(100)
);

create table ResourceValues(
	id serial primary key,
	languageId int references Languages(id),
	codeID int references ResourceCode(id),
	value varchar(255),
	deleteDate timestamp
);

create table PassportNumberType(
	id serial primary key,
	typeNameCodeId int references ResourceCode(id)
);

create table TicketPerson(
	id serial primary key,
	firstName varchar,
	lastName varchar,
	secondName varchar,
	passporNumber varchar,
	passportNumberType int references PassportNumberType(id)
);

create table TicketStatus(
	id serial primary key,
	nameCodeId int references ResourceCode(id)
);

create table OrderStatus(
	id serial primary key,
	nameCodeId int references ResourceCode(id)
);


create table ScheduleType(
	id serial primary key,
	nameCodeId int references ResourceCode(id)
);

create table BusType(
	id serial primary key,
	nameCodeId int references ResourceCode(id),
	capacity int
);

create table Bus(
	id serial primary key,
	name varchar,
	busTypeId int references BusType(id)
);

create table LocationType(
	id serial primary key,
	nameCodeId int references ResourceCode(id)
);

create table Location(
	id serial primary key,
	coordinates varchar,
	locationTypeId int references LocationType(id),
	nameCodeId int references ResourceCode(id)
);

create table Route(
	id serial primary key,
	destinationLocationId int references Location(id),
	sourceLocationId int references Location(id),
	distance float
);

create table Schedule(
	id serial primary key,
	scheduleNumber varchar,
	creationDate timestamp,
	weekDay int,
	beginDate timestamp,
	endDate timestamp,
	isActive bool,
	deleteDate timestamp,
	scheduleTypeId int references ScheduleType(id),
	routeId int references Route(id),
	busId int references Bus(id),
	driverId int references Users(id)
);

create table Orders(
	id serial primary key,
	userId int references Users(id),
	scheduleId int references Schedule(id),
	orderStatusId int references OrderStatus(id),
	totalPrice decimal(12, 3)
);

create table Ticket(
	id serial primary key,
	creationDate timestamp,
	seatNumber int,
	orderId int references Orders(id),
	ticketPersonId int references TicketPerson(id),
	routeId int references Route(id),
	ticketStatus int references TicketStatus(id)
);

create table TouristTrip(
	id serial primary key,
	titleNameCodeId int references ResourceCode(id),
	descriptionNameCodeId int references ResourceCode(id),
	ownerId int references Users(id),
	price decimal(12, 3),
	deleteDate timestamp,
	guideId int references Users(id),
	scheduleId int references Schedule(id)
);
