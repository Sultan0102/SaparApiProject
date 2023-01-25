insert into Roles(roleName)
values
(1, 'Admin'),
(2, 'Customer'),
(3, 'Guide'),
(4, 'BusinessPerson');

insert into Users(id, email, password, firstName, lastName, birthDate, isdeleted, roleID)
values
(1, 'anuar@mail.ru', 'anuar123', 'Anuar', 'Bora', '2001-10-12', 'false', 1),
(2, 'elvira@mail.ru', 'elvira123', 'Elvira', 'Nuga', '2000-10-12', 'false', 2),
(3, 'sultan@mail.ru', 'sultan123', 'Sultan', 'Rahma', '2001-10-12', 'false', 3),
(4, 'jandos@mail.ru', 'jandos123', 'Jandos', 'Bakit', '2001-10-12', 'false', 4);

insert into ResourceCode(id, defaultValue)
values
(1, 'Russian'),
(2, 'Kazakh'),
(3, 'English'),
(4, 'Almaty'),
(5, 'Taraz'),
(6, 'Pavlodar'),
(7, 'Astana'),
(8, 'Shymkent'),
(9, 'Oskemen'),
(10, 'Aktobe'),
(11, 'Single Deck Bus'),
(12, 'City'),
(13, 'Tourist Attraction');


insert into Languages(id, nameCodeId, nativeName)
values
(1, 1, 'Русский'),
(2, 2, 'Қазақ'),
(3, 3, 'English');


insert into ResourceValues(id, codeId, languageId, value)
values
(1, 1, 1, 'Русский'),
(2, 1, 2, 'Орыс'),
(3, 1, 3, 'Russian'),
(4, 2, 1, 'Казахский'),
(5, 2, 2, 'Қазақ'),
(6, 2, 3, 'Kazakh'),
(7, 4, 1, 'Алматы'),
(8, 4, 2, 'Алматы'),
(9, 4, 3, 'Almaty'),
(10, 5, 1, 'Тараз'),
(11, 5, 2, 'Тараз'),
(12, 5, 3, 'Taraz'),
(13, 6, 1, 'Павлодар'),
(14, 6, 2, 'Павлодар'),
(15, 6, 3, 'Pavlodar'),
(16, 7, 1, 'Астана'),
(17, 7, 2, 'Астана'),
(18, 7, 3, 'Astana'),
(19, 8, 1, 'Шымкент'),
(20, 8, 2, 'Шымкент'),
(21, 8, 3, 'Shymkent'),
(22, 9, 1, 'Усть Каменогорск'),
(20, 9, 2, 'Өскемен'),
(21, 9, 3, 'Oskemen'),
(19, 10, 1, 'Актобе'),
(20, 10, 2, 'Ақтөбе'),
(21, 10, 3, 'Aktobe'),
(22, 11, 1, 'Одноэтажный'),
(23, 11, 2, 'Бір қабатты'),
(24, 11, 3, 'Single Deck'),
(25, 12, 1, 'Город'),
(26, 12, 2, 'Қала'),
(27, 12, 3, 'City'),
(28, 13, 1, 'Достопримечательность'),
(28, 13, 1, 'Туристік Тартымдылық'),
(28, 13, 1, 'Tourist Attraction');

insert into BusType(id, namecodeid, capacity)
values
(1, 11, 40);

insert into Bus(id, name, bustypeid)
values
(1, 'SomeBus1', 1);

select * from LocationType
insert into LocationType(id, nameCodeId)
values
(1, 12),
(2, 13);

insert into Location(id, coordinates, locationTypeId, nameCodeId)
values
(1, '43.2220, 76.8512', 1, 4),
(2, '42.8984, 71.3980', 1, 5),
(3, '52.2873, 76.9674', 1, 6),
(4, '51.1605, 71.4704', 1, 7),
(5, '42.3417, 69.5901', 1, 8),
(6, '49.9749, 82.6017', 1, 9);
(7, '50.2839, 57.1670', 1, 10);

insert into Route(id, sourceLocationId, destinationLocationId, distance)
values(1, 1, 2, 1000),
(2, 2, 1, 2000),
(3, 1, 3, 3000),
(4, 3, 1, 4000),
(5, 4, 3, 5000),
(6, 2, 4, 6000),
(7, 4, 1, 7000),
(8, 7, 2, 8000),
(9, 3, 7, 7000),
(10, 5, 1, 9000);

