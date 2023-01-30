import tkinter as tk
from tkinter import ttk
import src.funcs
import datetime
import src.globals as g


def FormatDate(d):
    dt = datetime.datetime.fromisoformat(d)
    return dt.strftime("%b %d, %Y")


def CheckoutWindow(master, room, callback):
    def onCheckout(tl):
        callback(True, tl)

    def onInvoice():
        BillWindow(master, room["occupied"], onCheckout)
        tl.destroy()

    tl = tk.Toplevel(master=master, background="#2D3033")
    tl.geometry("400x500")

    ttk.Label(tl, text="CHECK OUT", font=("Barlow", 16)).place(
        relx=0.1, rely=0.15)

    ttk.Label(tl, text="Confirm checkout", font=("Barlow", 16), justify="left", anchor="s").place(
        relx=0.1, rely=0.2, relheight=0.2)

    ttk.Label(tl, text=room["guest"], font=("Barlow", 20, "bold"), justify="left").place(
        relx=0.1, rely=0.4, relheight=0.1)
    ttk.Label(tl, text="Currently in room " + str(room["room"]), font=("Barlow", 15), justify="left", anchor="n").place(
        relx=0.1, rely=0.55, relheight=0.1)

    checkoutButton = ttk.Button(
        tl, text="Check Out", command=lambda: onCheckout(tl), style="Primary.TButton")
    checkoutButton.place(relx=0.1, rely=0.75, relwidth=0.80, relheight=0.08)

    invoiceButton = ttk.Button(
        tl, text="Generate Invoice", command=onInvoice)
    invoiceButton.place(relx=0.1, rely=0.85, relwidth=0.80, relheight=0.08)


def CheckinWindow(master, room, callback):
    def onCheckin(guestName):
        if guestName != "Barlow":
            callback(guestName, tl)

    tl = tk.Toplevel(master=master, background="#2D3033")
    tl.geometry("400x500")

    ttk.Label(tl, text="CHECK IN", font=("Barlow", 16)).place(
        relx=0.1, rely=0.15)

    ttk.Label(tl, text="Guest Name", font=("Barlow", 16)).place(
        relx=0.1, rely=0.4, relheight=0.1)

    e = ttk.Entry(tl, font=("Barlow", 20),
                  background="#eeeeee", justify="left")
    e.place(relx=0.1, rely=0.5, relheight=0.10, relwidth=0.8)

    checkoutButton = ttk.Button(
        tl, text="Check in", command=lambda: onCheckin(e.get()), style="Primary.TButton")
    checkoutButton.place(relx=0.1, rely=0.85, relwidth=0.80, relheight=0.08)


def BillWindow(master, guestId, callback):
    tl = tk.Toplevel(master=master, background="#2D3033")
    tl.geometry("400x600")

    guestInfo = src.funcs.GetGuestData(guestId)

    if guestInfo["checked_out"] == None:
        guestInfo["checked_out"] = datetime.datetime.isoformat(g.appDate)

    d1 = datetime.datetime.fromisoformat(guestInfo["checked_in"])
    d2 = datetime.datetime.fromisoformat(guestInfo["checked_out"])

    ttk.Label(tl, text="INVOICE FOR", font=("Barlow", 16),
              anchor="w").place(relx=0.1, rely=0.15)
    ttk.Label(tl, text=guestInfo["name"], font=(
        "Barlow", 24), anchor="w").place(relx=0.1, rely=0.2)

    ttk.Label(tl, text="Checked In", font=("Barlow", 16), anchor="w").place(
        relx=0.1, rely=0.3, relwidth=0.4)
    ttk.Label(tl, text=FormatDate(guestInfo["checked_in"]), font=(
        "Barlow", 16), anchor="e").place(relx=0.5, rely=0.3, relwidth=0.4)

    ttk.Label(tl, text="Checked Out", font=("Barlow", 16), anchor="w").place(
        relx=0.1, rely=0.35, relwidth=0.4)
    ttk.Label(tl, text=FormatDate(guestInfo["checked_out"]), font=(
        "Barlow", 16), anchor="e").place(relx=0.5, rely=0.35, relwidth=0.4)

    daysStayed = (d2 - d1).days
    ttk.Label(tl, text="Days Stayed", font=("Barlow", 16), anchor="w").place(
        relx=0.1, rely=0.6, relwidth=0.4)
    ttk.Label(tl, text=str(daysStayed) + " days", font=("Barlow", 16),
              anchor="e").place(relx=0.5, rely=0.6, relwidth=0.4)

    ttk.Label(tl, text="Rate per Day", font=("Barlow", 16), anchor="w").place(
        relx=0.1, rely=0.55, relwidth=0.4)
    ttk.Label(tl, text=str(g.rate), font=("Barlow", 16), anchor="e").place(
        relx=0.5, rely=0.55, relwidth=0.4)

    totalCost = daysStayed * g.rate
    ttk.Label(tl, text="Total Charges", font=("Barlow", 16), anchor="w").place(
        relx=0.1, rely=0.65, relwidth=0.4)
    ttk.Label(tl, text=str(totalCost), font=("Barlow", 16), anchor="e").place(
        relx=0.5, rely=0.65, relwidth=0.4)

    closeButton = ttk.Button(
        tl, text="Close", command=lambda: callback(tl), style="Primary.TButton")
    closeButton.place(
        relx=0.1, rely=0.82, relwidth=0.8, relheight=0.08)
