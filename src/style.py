from tkinter import ttk


def TtkStyles(master):
    style = ttk.Style(master)
    style.theme_use('default')

    style.configure(".", font=("Barlow",))
    style.configure("TButton", foreground="#ffffff", background="#2D3033")
    style.map("TButton", foreground=[("!active", "#ffffff"), ("active", "#ffffff")], background=[("active", "#2D3033"), ("!active", "#2D3033")])
    style.configure("TButton", relief="flat", bd=2, border="blue", font=("Barlow", 17, "bold"))

    style.configure("TLabel", foreground="#ffffff", background="#2D3033", anchor="center", font=("Barlow", 17))

    style.configure("Primary.TButton", foreground="#ffffff", background="#ff9913", font=("Barlow", 17, "bold"))
    # style.configure("TButton", borderwidth=3, relief="flat",
                    # foreground="#ffffff", background="#ff9913", border=2, bordercolor="white")
