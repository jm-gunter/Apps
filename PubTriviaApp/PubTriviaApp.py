# JGunter 5/13/16

try:
    from sqlalchemy import *
    from tkinter import *
    from tkinter import ttk
    import datetime
    import PTConfig
    from ViewLibrary.GameView import *

except ImportError:
    from sqlalchemy import *
    from Tkinter import *
    import ttk
    import datetime
    import PTConfig
    from ViewLibrary.GameView import *


def main():

    root = Tk()  # create a Tk root window

    # Pop the window to the front on startup.
    # For development only, this will not be necessary
    # once PubTriviaApp is bundled as an OSX app
    root.attributes('-topmost', True)

    # Setup the root to appear in the middle of the screen
    d_size = (850, 500)
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (d_size[0], d_size[1], (ws/2) - (d_size[0]/2), (hs/2) - (d_size[1]/2)))
    root.title('Pub Trivia Host')
    app = GameView(root, rounds=5, teams=5)

    # Run
    root.mainloop()

if __name__ == '__main__':
    main()

