DROP TABLE IF EXISTS temp_unpaid_orders;

CREATE TEMP TABLE temp_unpaid_orders(
	id serial primary key
);

INSERT INTO temp_unpaid_orders
SELECT id 
FROM "Order" 
WHERE "isPaid" = false
AND abs(EXTRACT(EPOCH FROM current_timestamp-"creationDate")/60) > 15;

DROP TABLE IF EXISTS temp_ticket_persons_to_be_deleted;
CREATE TEMP TABLE temp_ticket_persons_to_be_deleted(
	id serial primary key
);

INSERT INTO temp_ticket_persons_to_be_deleted
SELECT person_id FROM "Ticket"
WHERE order_id in (SELECT id from temp_unpaid_orders)
AND person_id is not null;

UPDATE "Ticket"
SET order_id = null,
	person_id = null,
	status_id = 3
WHERE order_id in (SELECT id from temp_unpaid_orders);

DELETE FROM "TicketPerson"
WHERE id in (SELECT id FROM temp_ticket_persons_to_be_deleted);

DELETE FROM "Order"
WHERE id in (SELECT id FROM temp_unpaid_orders);
	