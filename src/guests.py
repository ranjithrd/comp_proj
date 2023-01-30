import tkinter as tk
from tkinter import ttk
import src.funcs
import datetime
import src.roomWindows as rw


def FormatDate(d):
    dt = datetime.datetime.fromisoformat(d)
    return dt.strftime("%b %d, %Y")


class GuestsWindow(tk.Frame):

    def onCheckoutDone(self, conf, room, tl):
        if not conf:
            return

        src.funcs.CheckoutGuest(room["occupied"], room["room"])

        tl.destroy()

        self.guestFrame.destroy()
        self.guestsElements()

    def onCheckoutClick(self, room):
        rw.CheckoutWindow(self.master, room, lambda x,
                          tl: self.onCheckoutDone(x, room, tl))

    def onInvoiceClick(self, room):
        rw.BillWindow(self.master, room["id"], lambda tl: tl.destroy())

    def guestsElements(self):
        guests = src.funcs.GetAllGuestsData()

        guestFrame = tk.Frame(self.master, background="#2D3033")
        guestFrame.place(relx=0, rely=0, relheight=1.0, relwidth=1.0)

        ttk.Label(guestFrame, text="Guests", font=("Barlow", 24, "bold")).place(
            relx=0.1, rely=0.08, relheight=0.08)

        guestsCanvas = tk.Canvas(
            guestFrame, background="#2D3033", bd=0, highlightthickness=0,)

        # SCROLLING LOGIC
        scrollArea = tk.Scrollbar(
            guestsCanvas, orient="vertical", command=guestsCanvas.yview)
        guestsCanvas.configure(yscrollcommand=scrollArea.set)
        f = tk.Frame(guestsCanvas)
        guestsCanvas.place(relx=0.1, rely=0.18, relwidth=0.8, relheight=0.72)
        guestsCanvas.bind("<Configure>", lambda e: guestsCanvas.configure(
            scrollregion=guestsCanvas.bbox("all")))
        guestsCanvas.create_window((0, 0), anchor='ne', window=f, width=720)
        scrollArea.place(relx=1, width=20, rely=0, relheight=1, anchor="ne")

        y = 10
        for guest in guests:
            gFrame = tk.Frame(guestsCanvas, background="#242629")

            tk.Label(gFrame, text=guest["name"], font=("Barlow", 20, "bold"), background="#242629", foreground="white").place(
                relx=0.05, rely=0.3, relheight=0.25)

            def l(room, l):
                return lambda: l(room)

            t = ""
            if guest["checked_out"] != None:
                t = "Checked in on " + \
                    FormatDate(
                        guest["checked_in"]) + " | Checked out on " + FormatDate(guest["checked_out"])
            else:
                t = "Checked in on " + \
                    FormatDate(guest["checked_in"]) + \
                    " | Staying in Room " + str(guest["room"])

                checkoutButton = ttk.Button(
                    gFrame, text="Checkout", command=l(guest, self.onCheckoutClick))
                checkoutButton.place(relx=0.9, rely=0.3,
                                     height="40px", relwidth=0.15, anchor="e")

            invoiceButton = ttk.Button(
                gFrame, text="Invoice", command=l(guest, self.onInvoiceClick))
            invoiceButton.place(relx=0.9, rely=0.6,
                                height="40px", relwidth=0.15, anchor="e")

            ttk.Label(gFrame, text=t, font=("Barlow", 16), background="#242629").place(
                relx=0.05, rely=0.55)

            guestsCanvas.create_window(
                -20, y, window=gFrame, width=680, height=150, anchor="ne")

            y += 175

        # guestsCanvas.create_text(10, 10, text="Hi")

        self.guestFrame = guestFrame

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master

        self.master.geometry("900x700")

        self.guestsElements()


def OpenGuestsScreen(master):
    screen = tk.Toplevel(master=master)
    GuestsWindow(screen)
