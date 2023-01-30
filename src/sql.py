CREATE_TABLES = '''

CREATE TABLE IF NOT EXISTS guests (
    id INT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    checked_in TIMESTAMP,
    checked_out TIMESTAMP
);

CREATE TABLE IF NOT EXISTS rooms (
    room INT PRIMARY KEY NOT NULL,
    occupied INT
);

'''

GET_ROOM_DATA = '''

SELECT room, occupied, name, checked_in, checked_out
FROM rooms
LEFT JOIN guests
ON rooms.occupied = guests.id;

'''

GET_ALL_GUESTS_DATA = '''

SELECT id, name, checked_in, checked_out, room, occupied
FROM guests
JOIN rooms
ON rooms.occupied = guests.id
ORDER BY room, checked_in ASC;

'''

GET_OLD_GUESTS_DATA = '''

SELECT id, name, checked_in, checked_out
FROM guests
WHERE checked_out IS NOT NULL
ORDER BY checked_out ASC;

'''

GET_GUEST_DATA = '''

SELECT * 
FROM guests
WHERE id = ?1;

'''

CHECK_IN_USER_1 = '''

INSERT INTO guests
(id, name, checked_in, checked_out)
VALUES (?1, ?2, ?3, ?4);

'''

CHECK_IN_USER_2 = '''

UPDATE rooms
SET occupied = ?1
WHERE room = ?2;

'''

CHECK_OUT_USER_1 = '''

UPDATE guests 
SET checked_out = ?1
WHERE id = ?2;

'''

CHECK_OUT_USER_2 = '''

UPDATE rooms
SET occupied = NULL
WHERE room = ?1;

'''

INSERT_GUEST = '''

INSERT INTO guests
(id, name, checked_in, checked_out)
VALUES (?1, ?2, ?3, ?4);

'''

INSERT_ROOM = '''

INSERT INTO rooms
(room, occupied)
VALUES (?1, ?2);

'''