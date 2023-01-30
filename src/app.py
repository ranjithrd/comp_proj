import tkinter as tk
from tkinter import ttk
import datetime
from PIL import Image, ImageTk

# File Imports
import src.rooms as rooms
import src.guests as guests
import src.help as help
import src.globals as g
import src.style

def RateChangePopup(master, callback):
    global g

    popup = tk.Toplevel(master=master, background="#2D3033")
    popup.title("Change Daily Rate")
    popup.geometry("400x400")

    label = ttk.Label(master=popup, text="Change Daily Rate",
                     font=("Barlow", 22, "bold"))
    label.place(relx=0.1, rely=0.2, relwidth=0.8)

    entry = tk.Entry(popup, justify="center", font=("Barlow", 18))
    entry.insert(0, str(g.rate))
    entry.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)

    button = ttk.Button(master=popup, text="Change", style="Primary.TButton",
                        command=lambda: callback(entry.get(), popup))
    button.place(relx=0.1, rely=0.85, relwidth=0.8, relheight=0.1)


class Window(tk.Frame):
    loggedIn = False

    def onLoginClick(self, entered):
        if entered == g.password:
            self.loggedIn = True
            self.loginFrame.destroy()
            self.homeElements()

        else:
            wrongLabel = tk.Label(self.loginFrame, text="Wrong password")
            wrongLabel.grid(row=5, column=1)

    def onLogoutClick(self):
        self.homeFrame.destroy()
        self.loginElements()
        self.loggedIn = False

    def onPrevClick(self):
        global g
        g.appDate -= g.day
        self.homeFrame.destroy()
        self.homeElements()

    def onNextClick(self):
        global g
        g.appDate += g.day
        self.homeFrame.destroy()
        self.homeElements()

    def onQuitClick(self):
        self.master.quit()

    def onChangeCallback(self, newRate, window):
        global g
        g.rate = int(newRate)
        window.destroy()
        self.homeFrame.destroy()
        self.homeElements()

    def onChangeClick(self):
        RateChangePopup(self.master, self.onChangeCallback)
        pass

    def homeElements(self):
        global g

        bgFrame = tk.Frame(self.master, background="#2D3033")
        bgFrame.place(relx=0, rely=0, relheight=1, relwidth=1)

        homeFrame = tk.Frame(bgFrame, background="#2D3033")
        homeFrame.place(relx=0.025, rely=0.025, relheight=0.95, relwidth=0.95)

        self.logoutSrc = Image.open(
            "./images/quit.png").resize((25, 25), Image.LANCZOS)
        self.logoutImg = ImageTk.PhotoImage(self.logoutSrc)
        logoutButton = ttk.Button(
            homeFrame, image=self.logoutImg, text="Logout", command=self.onLogoutClick)
        logoutButton.place(relx=0, rely=0.15, relwidth=0.25, relheight=0.15)

        dateString = "Today: " + \
            str(g.appDate.month) + "/" + str(g.appDate.day)
        dateLabel = ttk.Label(homeFrame, text=dateString, justify="center")
        dateLabel.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.15)

        quitButton = ttk.Button(homeFrame, text="Quit",
                                command=self.onQuitClick)
        quitButton.place(relx=0, rely=0, relwidth=0.25, relheight=0.15)

        self.prevSrc = Image.open(
            "./images/prev.png").resize((25, 25), Image.LANCZOS)
        self.prevImg = ImageTk.PhotoImage(self.prevSrc)
        prevButton = ttk.Button(homeFrame, text="Prev Day", image=self.prevImg,
                                command=self.onPrevClick)
        prevButton.place(relx=0.25, rely=0.15, relwidth=0.25, relheight=0.15)

        self.nextSrc = Image.open(
            "./images/next.png").resize((25, 25), Image.LANCZOS)
        self.nextImg = ImageTk.PhotoImage(self.nextSrc)
        nextButton = ttk.Button(homeFrame, text="Next Day", image=self.nextImg,
                                command=self.onNextClick)
        nextButton.place(relx=0.5, rely=0.15, relwidth=0.25, relheight=0.15)

        self.roomsSrc = Image.open(
            "./images/rooms.png").resize((170, 170), Image.LANCZOS)
        self.roomsImg = ImageTk.PhotoImage(self.roomsSrc)
        RoomsButton = ttk.Button(homeFrame, image=self.roomsImg,
                                 command=lambda: rooms.OpenCheckinScreen(self.master))
        RoomsButton.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.5)

        self.guestsSrc = Image.open(
            "./images/guests.png").resize((170, 170), Image.LANCZOS)
        self.guestsImg = ImageTk.PhotoImage(self.guestsSrc)
        GuestsButton = ttk.Button(homeFrame, text="Guests", image=self.guestsImg,
                                  command=lambda: guests.OpenGuestsScreen(
                                      self.master)
                                  )
        GuestsButton.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.5)

        self.helpSrc = Image.open(
            "./images/help.png").resize((50, 50), Image.LANCZOS)
        self.helpImg = ImageTk.PhotoImage(self.helpSrc)
        HelpButton = ttk.Button(homeFrame, text="Help", image=self.helpImg, command=lambda: help.HelpScreen(self.master))
        HelpButton.place(relx=0.0, rely=0.8, relwidth=1.0, relheight=0.2)

        rateText = "Rate: " + str(g.rate)
        rateLabel = ttk.Label(homeFrame, text=rateText)
        rateLabel.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.15)

        self.rateSrc = Image.open(
            "./images/rate.png").resize((25, 25), Image.LANCZOS)
        self.rateImg = ImageTk.PhotoImage(self.rateSrc)
        changeRateButton = ttk.Button(homeFrame, text="Change Rate", image=self.rateImg,
                                      command=self.onChangeClick)
        changeRateButton.place(relx=0.75, rely=0.15,
                               relwidth=0.25, relheight=0.15)

        self.homeFrame = homeFrame

    def loginElements(self):
        loginFrame = tk.Frame(self.master, background="#2D3033")
        loginFrame.place(rely=0, relx=0, relwidth=1.0, relheight=1.0)

        ttk.Label(loginFrame, text="Doorman", font=("Barlow", 24, "bold")).place(
            rely=0.1, relx=0.1, relwidth=0.8)

        label = ttk.Label(
            loginFrame, text="Log in to Doorman", font=("Barlow", 18))
        label.place(rely=0.375, relx=0.1, relwidth=0.8)

        enteredPassword = tk.StringVar()
        input = ttk.Entry(loginFrame, textvariable=enteredPassword,
                          show="*", font=("Barlow", 20), justify="center")
        input.place(rely=0.5, relx=0.1, relwidth=0.8, relheight=0.1)

        loginButton = ttk.Button(
            loginFrame, text="Log in", command=lambda: self.onLoginClick(enteredPassword.get()), style="Primary.TButton")
        loginButton.place(rely=0.8, relx=0.1, relwidth=0.8, relheight=0.1)

        self.loginFrame = loginFrame

    def __init__(self, master=None):
        tk.Frame.__init__(self, master, background="#2D3033")
        self.master = master

        master.geometry("500x400")

        if self.loggedIn:
            self.homeElements()
        else:
            self.loginElements()

    def clearFrame(self):
        self.loginFrame.destroy()
        for widget in self.winfo_children():
            widget.destroy()


def StartApp():
    print("D O O R M A N")

    root = tk.Tk()
    app = Window(root)
    src.style.TtkStyles(app)

    root.wm_title("Doorman")
    root.mainloop()
