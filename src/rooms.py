import tkinter as tk
from tkinter import ttk
import src.roomWindows as rw
import src.funcs


class RoomsWindow(tk.Frame):
    guests = []

    def onCheckoutDone(self, conf, room, tl):
        if not conf:
            return

        src.funcs.CheckoutGuest(room["occupied"], room["room"])

        tl.destroy()

        self.roomsFrame.destroy()
        self.roomsElements()

    def onCheckinDone(self, guestName, room, tl):
        src.funcs.CheckinGuest(guestName, room["room"])

        tl.destroy()

        self.roomsFrame.destroy()
        self.roomsElements()

    def onCheckoutClick(self, room):
        rw.CheckoutWindow(self.master, room, lambda x,
                          tl: self.onCheckoutDone(x, room, tl))

    def onCheckinClick(self, room):
        rw.CheckinWindow(self.master, room, lambda x,
                         tl: self.onCheckinDone(x, room, tl))

    def roomsElements(self):
        rooms = src.funcs.GetRoomData()

        roomsFrame = tk.Frame(master=self.master, background="#2D3033")
        roomsFrame.place(relheight=1.0, relwidth=1.0, relx=0, rely=0)
        self.roomsFrame = roomsFrame

        title = ttk.Label(roomsFrame, text="Rooms",
                          font=("Barlow", 24, "bold"))
        title.place(relx=0.1, rely=0.45, relheight=0.1)

        for room in rooms:
            roomFrame = tk.Frame(master=roomsFrame,
                                 relief="groove", borderwidth=1, background="#242629")

            innerFrame = tk.Frame(master=roomFrame, background="#242629")

            numberLabel = ttk.Label(
                innerFrame, text="Room " + str(room["room"]), font=("Barlow", 25), background="#242629")
            numberLabel.pack()

            def l(room, l):
                return lambda x: l(room)

            if room["occupied"]:
                occupiedLabel = ttk.Label(
                    innerFrame, text="Occupied by " + room["guest"], background="#242629")
                occupiedLabel.pack()

                ctaLabel = ttk.Label(
                    innerFrame, text="Click to check out", background="#242629")
                ctaLabel.pack()

                roomFrame.bind("<Button>", l(room, self.onCheckoutClick))
                innerFrame.bind("<Button>", l(room, self.onCheckoutClick))

            else:
                emptyLabel = ttk.Label(
                    innerFrame, text="Unoccupied", background="#242629")
                emptyLabel.pack()

                ctaLabel = ttk.Label(
                    innerFrame, text="Click to check in", background="#242629")
                ctaLabel.pack()

                roomFrame.bind("<Button>", l(room, self.onCheckinClick))
                innerFrame.bind("<Button>", l(room, self.onCheckinClick))

            innerFrame.place(relx=0, rely=0.35, relheight=0.5, relwidth=1)

            colwidth = 2/len(rooms)
            if (room["room"] <= len(rooms)/2):
                col = room["room"] - 1
                roomFrame.place(relheight=0.4, relwidth=colwidth,
                                rely=0, relx=col*colwidth)
            else:
                col = room["room"] - len(rooms)/2 - 1
                roomFrame.place(relheight=0.4, relwidth=colwidth,
                                rely=0.6, relx=col*colwidth)

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master

        master.geometry("900x700")

        self.roomsElements()


def OpenCheckinScreen(master):
    screen = tk.Toplevel(master=master)
    RoomsWindow(screen)
