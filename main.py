import src.app
import src.funcs

def Main():
    src.funcs.StartDatabase()
    src.funcs.FillDefaultRooms()

    print("GUEST MANAGER")

    src.app.StartApp()

if __name__ == "__main__":
    Main()
