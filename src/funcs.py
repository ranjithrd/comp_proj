import src.sql as sql
import sqlite3
import src.defaultRooms
import datetime
import random
import math
import src.globals as g

# db = sqlite3.connect("proj.db")
db = None  # type: sqlite3.Connection


def RandomId():
    return math.floor(random.random() * 10e6)


def StartDatabase():
    global db

    db = sqlite3.connect("proj.db")

    db.executescript(sql.CREATE_TABLES)
    db.commit()

    print("Connected to database!")


def GetAllGuestsData():
    cursorCurrent = db.execute(sql.GET_ALL_GUESTS_DATA)
    recordsCurrent = cursorCurrent.fetchall()

    cursorOld = db.execute(sql.GET_OLD_GUESTS_DATA)
    recordsOld = cursorOld.fetchall()

    records = recordsCurrent + recordsOld

    retVal = []
    for rec in records:
        d = {
            "id": rec[0],
            "name": rec[1],
            "checked_in": rec[2],
            "checked_out": rec[3],
        }

        if d["checked_out"] == None:
            d["room"] = rec[4]
            d["occupied"] = rec[5]
            d["guest"] = rec[1]

        retVal.append(d)

    return retVal


def GetRoomData():
    cursor = db.execute(sql.GET_ROOM_DATA)
    records = cursor.fetchall()

    retVal = []
    for rec in records:
        d = {
            "room": rec[0],
            "occupied": rec[1],
            "guest": rec[2],
            "checked_in": rec[3],
            "checked_out": rec[4]
        }

        if d["occupied"] == None:
            d["occupied"] = ""

        retVal.append(d)

    return retVal


def GetGuestData(guestId):
    cursor = db.execute(sql.GET_GUEST_DATA, [guestId])
    rec = cursor.fetchone()

    if not rec:
        print("GUEST DOES NOT EXIST")
        return None

    return {
        "id": rec[0],
        "name": rec[1],
        "checked_in": rec[2],
        "checked_out": rec[3],
    }


def CheckinGuest(guestName, roomNumber):
    id = RandomId()
    db.execute(sql.CHECK_IN_USER_1, [
        id,
        guestName,
        g.appDate,
        None
    ])
    db.execute(sql.CHECK_IN_USER_2, [
        id,
        roomNumber
    ])
    db.commit()


def CheckoutGuest(guestId, roomNumber):
    db.execute(sql.CHECK_OUT_USER_1, [
        g.appDate,
        guestId,
    ])
    db.execute(sql.CHECK_OUT_USER_2, [
        roomNumber
    ])
    db.commit()


def FillDefaultRooms():
    currentRoomData = GetRoomData()

    if len(currentRoomData) > 0:
        return

    defRooms = src.defaultRooms.defaultRooms

    rooms = []
    guests = []

    for i in defRooms:
        if i["occupied"] == True:
            guests.append({
                "name": i["guest"],
                "room": i["room"]
            })

    for i in defRooms:
        d = {
            "room": i["room"],
            "occupied": None
        }

        rooms.append(d)

    for i in guests:
        id = RandomId()
        rooms[i["room"]]["occupied"] = id
        db.execute(sql.INSERT_GUEST, [id, i["name"], g.appDate, None])
        db.commit()

    for i in rooms:
        print("Filling in", i)
        db.execute(sql.INSERT_ROOM, [i["room"], i["occupied"]])
        db.commit()

    print("Filled in default rooms!")

    GetRoomData()
