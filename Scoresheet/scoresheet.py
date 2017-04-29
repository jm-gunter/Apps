import sys
import time
import tkinter as tk
from tkinter import font, messagebox, ttk
from game import Game

class Scoresheet(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)

        self._settings = kwargs.get('settings', dict())
        self._settings['padding'] = kwargs.get('padding', 2)
        self._settings['title_font'] = kwargs.get('title_font', font.Font(size=24))
        self._settings['header_font'] = kwargs.get('header_font', font.Font(size=16))
        self._game = kwargs.get('game', Game(12, 5))
        self._totals = list()
        self._team_names = list()
        self._menu = tk.Menu(self)

        # setup main window
        self.title("Trivia Scratch")
        self.geometry("500x345")
        self.iconbitmap('favicon.ico')
        self.config(menu=self._menu)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # file menu
        filemenu = tk.Menu(self._menu)
        filemenu.add_command(label="New", command=self.new_game)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.close)
        self._menu.add_cascade(label="File", menu=filemenu)

        # edit menu
        editmenu = tk.Menu(self._menu)
        self._menu.add_cascade(label="Edit", menu=editmenu)

        # view menu
        viewmenu = tk.Menu(self._menu)
        thememenu = tk.Menu(viewmenu)
        # add default themes
        for name in ttk.Style().theme_names():
            thememenu.add_command(label=name, command=lambda theme_name=name: self.set_theme(theme_name))
        #thememenu.add_separator()
        ## add custom themes
        #for theme in self.custom_themes:
        #    thememenu.add_command(label=name)
        viewmenu.add_cascade(label="Themes", menu=thememenu)
        self._menu.add_cascade(label="View", menu=viewmenu)

        # help menu
        helpmenu = tk.Menu(self._menu)
        self._menu.add_cascade(label="Help", menu=helpmenu)

        # Set up the main window's layout which consists of a header,
        # footer, content pane on left, and info pane on right.

        # header
        self._hframe = ttk.Frame(self)
        self._hframe.grid(row=0, column=0, columnspan=3, sticky="nesw")
        ttk.Label(self._hframe, text="Scratch", font=self._settings['title_font']).pack(side="left")
        separator = ttk.Separator(self, orient="horizontal").grid(row=1, column=0, columnspan=3, sticky="nesw")

        # content
        self._cframe = ttk.Frame(self)
        self._cframe.grid(row=2, column=0, sticky="nesw")

        # info
        separator = ttk.Separator(self, orient="vertical").grid(row=2, column=1, sticky="NESW")
        self._iframe = ttk.Frame(self)
        self._iframe.grid(row=2, column=2, sticky="nesw")
        ttk.Label(self._iframe, text="Standings", font=self._settings['header_font']).grid(row=0, column=0, sticky="w")

        # footer
        separator = ttk.Separator(self, orient="horizontal").grid(row=3, column=0, columnspan=3, sticky="NESW")
        self._fframe = ttk.Frame(self)
        self._fframe.grid(row=4, column=0, columnspan=3, sticky="nesw")
        ttk.Label(self._fframe, text="Trivia Scratch | Version 0:0:0").pack(side="left")

        self.setup_content(self._cframe, self.game)


    @property
    def settings(self):
        """A dictionary containing settings for the form.
            Settings include:
                padding: an integer to set the default padding used on all sides of widgets
                header_font: the font to use for header labels
        """
        return self._settings

    @settings.setter
    def settings(self, value):
        self._settings = value

    @property
    def game(self):
        """The game object used to setup the form widgets."""
        return self._game

    @game.setter
    def game(self, value):
        self._game = value

    def new_game(self):
        pass

    def import_game(self):
        pass

    def close(self):
        """Close app."""
        self.destroy()

    def set_theme(self, name):
        ttk.Style().theme_use(name)

    def setup_content(self, frame, game):
        """Create the appropriate number of entry widgets and
        labels for the passed game and assign bindings"""

        pad = self.settings['padding']
        hfont = self.settings['header_font']

        # clear any existing widgets and containers
        self._totals[:] = []
        self._team_names[:] = []
        for w in frame.winfo_children():
            w.destroy();

        # setup headers
        team_header = ttk.Frame(frame)
        team_header.grid(row=0, column=0, columnspan=3, sticky="nesw")
        ttk.Label(team_header, text="Teams", font=hfont).grid(row=0, column=0, sticky="nesw")
        add_team_btn = ttk.Button(team_header, text="+", command=lambda: self.add_team_btn_click(game))
        add_team_btn.grid(row=0, column=1, sticky="nesw")
        remove_team_btn = ttk.Button(team_header, text="-", command=lambda: self.remove_team_btn_click(game))
        remove_team_btn.grid(row=0, column=2, sticky="nesw")

        round_header = ttk.Frame(frame)
        round_header.grid(row=0, column=3, columnspan=game.rounds+1, sticky="nesw")
        ttk.Label(round_header, text="Rounds", font=hfont).grid(row=0, column=0, sticky="nesw")
        add_round_btn = ttk.Button(round_header, text="+", command=lambda: self.add_round_btn_click(game))
        add_round_btn.grid(row=0, column=1, sticky="nesw")
        remove_round_btn = ttk.Button(round_header, text="-", command=lambda: self.remove_round_btn_click(game))
        remove_round_btn.grid(row=0, column=2, sticky="nesw")

        # team-round score entry
        ttk.Label(frame, text="Team Name").grid(row=1, column=0, padx=pad, pady=pad, columnspan=2)
        ttk.Label(frame, text="# Players").grid(row=1, column=2, padx=pad, pady=pad)
        for i in range(game.teams):
            ttk.Label(frame, text=i+1).grid(row=i+2, column=0, sticky="E", padx=pad, pady=pad)
            namevar = tk.StringVar()
            ttk.Entry(frame, textvariable=namevar).grid(row=i+2, column=1, sticky="NESW", padx=pad, pady=pad)
            self._team_names.append(namevar)
            ttk.Entry(frame, width=5).grid(row=i+2, column=2, sticky="NESW", padx=pad, pady=pad)
            for j in range(game.rounds):
                ttk.Label(frame, text=j+1).grid(row=1, column=j+3, padx=pad, pady=pad)
                # Round Score field
                e1 = ttk.Entry(frame, width=5)
                e1.grid(row=i+2, column=j+3, sticky="NESW", padx=pad, pady=pad)
                e1.bind("<KeyRelease>", lambda event, sender=e1, team=i, round=j: self.update_score(event, sender, team, round))
                #e1.bind("<KeyRelease>", lambda event, row=i+2, column=j+3: self.key_release(event, scoresheet, row, column))

            textvar = tk.StringVar()
            ttk.Entry(frame, textvariable=textvar, width=5).grid(row=i+2, column=game.rounds+3, sticky="NESW", padx=pad, pady=pad)
            self._totals.append(textvar)
        ttk.Label(frame, text="Total").grid(row=1, column=game.rounds+3, padx=pad, pady=pad)

        self.update_standings()
        self.geometry('') # resets scoresheet geometry to fit widgets

    #def key_release(self, event, frame, row, column):
    #    if event.keysym == "Left" or event.keysym == "Tab":
    #        w = self.find_in_grid(frame, row, column-1)
    #        w.focus()
    #    elif event.keysym == "Right":
    #        pass
    #    elif event.keysym == "Up":
    #        pass
    #    elif event.keysym == "Down" or event.keysym == "Return":
    #        pass

    #def find_in_grid(self, frame, row, column):
    #    for child in frame.children.values():
    #        info = frame.grid_info()
    #        # note that rows and column numbers are stored as string
    #        for widget in info:
    #            if widget['row'] == str(row) and widget['column'] == str(column):
    #                return widget
    #    return None

    def update_score(self, event, sender, team, round):
        try:
            score = int(sender.get())
        except:
            score = 0
        self.game.set_score(team, round, score)
        self._totals[team].set(self.game.team_totals[team])
        self.update_standings()

    def update_standings(self):
        """Calculate standings and post them to the info frame. """

        # build a list of (team index, score) sorted by descending score
        standings = []
        for i in range(len(self._totals)):
            try:
                score = int(self._totals[i].get())
            except:
                score = 0
            standings.append((i, score))
        standings = sorted(standings, key=lambda x: x[1], reverse=True)

        # clear any existing labels
        for w in self._iframe.winfo_children():
            if w.cget("text") != "Standings":
                w.destroy();

        # Lookup the team name for each score and post to self._iframe
        for i in range(len(standings)):
            ts = standings[i]
            # set gold color for top 2 places
            fcolor = "#ECAC00" if i < 2 else "#000000"
            # set green for a tie
            priorscore = -1
            nextscore = -1
            if i > 0:
                priorscore = standings[i-1][1]
            if i < len(standings)-1:
                nextscore = standings[i+1][1]
            if (ts[1] == priorscore or ts[1] == nextscore):
                fcolor = "#3DC518"
            team = self._team_names[ts[0]].get()
            if (team):
                msg = "#{0}: {1} - {2}pts".format(i+1, team, ts[1])
                ttk.Label(self._iframe, text= msg, foreground=fcolor, padding=self._settings['padding']).grid(row=i+1, column=0, sticky="w")

        self.geometry('') # resets scoresheet geometry to fit widgets


    def add_team_btn_click(self, game):
        """Add one team."""
        game.teams += 1
        self.setup_content(self._cframe, game)

    def remove_team_btn_click(self, game):
        """Remove one team."""
        if game.teams > 1:
            game.teams -= 1
            self.setup_content(self._cframe, game)
        else:
            messagebox.showinfo("CANNOT REMOVE", "Game must have at least one team.")

    def add_round_btn_click(self, game):
        """Add one round."""
        game.rounds += 1
        self.setup_content(self._cframe, game)

    def remove_round_btn_click(self, game):
        """Remove one round."""
        if game.rounds > 1:
            game.rounds -= 1
            self.setup_content(self._cframe, game)
        else:
            messagebox.showinfo("CANNOT REMOVE", "Game must have at least one round.")


if __name__=='__main__':
    try:
        if len(sys.argv) > 1:
            if len(sys.argv) == 3:
                app=Scoresheet(game=Game(int(sys.argv[1]), int(sys.argv[2])))
            else:
                raise ValueError('scoresheet.py should be called with zero or two args.')
        else:
            app = Scoresheet()
        app.mainloop()
    except ValueError as e:
        print()
        print("Error: " + str(e))
        print()
