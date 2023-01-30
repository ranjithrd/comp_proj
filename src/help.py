import tkinter as tk
from tkinter import ttk

HELP_TEXT = '''
Doorman is made with Tkinter and stores all data in a SQLite database. 
Find help on how to use it below.

CHECKING GUESTS IN
Click the "Rooms" button in the main window and click any room that you'd like to 
check a guest into. Then, enter their name in the popup.
The newly added guest will be visible in the Rooms window as well as the Guests 
window.

CHECKING GUESTS OUT
Guests can be checked out from both the Guests and Rooms screens. 
In the Rooms window, click the room with the guest's name and click "Check Out".
Alternatively, open the Guests window and click "Checkout" next to the guest's 
name.

GENERATING INVOICES
Invoices are available as soon as you check any guest out in the pop-up window 
shown.
To generate another, open the Guests window and click "Generate Invoice" for any 
guest.

MODIFYING DAILY RATE
In the Home window, click the "$" icon below "Rate: XXX" to open a popup where you 
can change the daily rate used to calculate prices in the invoice.

LOGGING OUT
Click the Exit icon below "Quit" in the Home window.

CHANGING THE DATE
Click the Forward or Backword icons in the Home Screen to change the date used 
in the app.

'''

def HelpScreen(master):
    screen = tk.Toplevel(master=master)
    screen.geometry("700x700")

    frame = tk.Frame(screen, background="#2D3033")
    frame.place(relx=0, rely=0, relheight=1, relwidth=1)

    ttk.Label(frame, text="How to Use Doorman", font=("Barlow", 24, "bold")).place(relx=0.1, rely=0.05, relheight=0.1, relwidth=0.8)
    ttk.Label(frame, text=HELP_TEXT, font=("Barlow", 14), anchor="n").place(relx=0.1, rely=0.15, relheight=0.95, relwidth=0.8)
