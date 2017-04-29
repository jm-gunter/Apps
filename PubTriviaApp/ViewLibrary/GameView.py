# JGunter 6/4/16
try:
    from tkinter import *
    from tkinter.ttk import *
    import datetime
    import PTConfig
    import ModelLibrary

except ImportError:
    from Tkinter import *
    import ttk
    import datetime
    import PTConfig
    import ModelLibrary


class GameView:

    def __init__(self, master, **kwargs):
        self._master = master
        self._num_rounds = kwargs['rounds'] if 'rounds' in kwargs else 5
        self._num_teams = kwargs['teams'] if 'teams' in kwargs else 5
        self._version = '1.0.0'
        self._main_window = ttk.Panedwindow(master, orient=VERTICAL)
        self._top_frame = ttk.Frame(self._main_window, padding=5, relief=RIDGE)
        self._bottom_frame = ttk.Frame(self._main_window, padding=5, relief=FLAT)

        # Main Window
        self._main_window.pack(fill=BOTH, expand=True)

        # Top Frame (ToolBar)
        search_field = ttk.Combobox(self._top_frame, width=20)
        search_field.pack(fill=X, side=LEFT)
        new_game_button = ttk.Button(self._top_frame, text='New Game')
        new_game_button.pack(fill=X, side=LEFT)
        close_game_button = ttk.Button(self._top_frame, text='Close Game')
        close_game_button.pack(fill=X, side=LEFT)
        save_game_button = ttk.Button(self._top_frame, text='Save Game')
        save_game_button.pack(fill=X, side=LEFT)
        add_team_button = ttk.Button(self._top_frame, text='Add Team', command=self.add_team_click)
        add_team_button.pack(fill=X, side=LEFT)
        remove_team_button = ttk.Button(self._top_frame, text='Remove Team')
        remove_team_button.pack(fill=X, side=LEFT)
        sort_teams_button = ttk.Button(self._top_frame, text='Sort Teams')
        sort_teams_button.pack(fill=X, side=LEFT)

        self._main_window.add(self._top_frame, weight=0)

        # Bottom Frame (Content)
        title = ttk.Label(self._bottom_frame, text='New Game', padding=1)
        title.pack(fill=X)
        title.config(font=('Helvetica', 24, 'bold'))
        # Setup columns
        label_frame = ttk.Frame(self._bottom_frame, relief=FLAT)
        ttk.Label(label_frame, width=1).pack(fill=X, expand=True, side=LEFT)
        ttk.Label(label_frame, text='Team Name', width=25).pack(fill=X, expand=True, side=LEFT)
        for r in range(1, self._num_rounds + 1):
            ttk.Label(label_frame, text='Round {}'.format(r), width=10).pack(fill=X, expand=True, side=LEFT)
        ttk.Label(label_frame, text='Total', padding=1, width=10).pack(fill=X, expand=True, side=LEFT)
        label_frame.pack(fill=X)
        # add rows for each team
        temp_row = 1
        while temp_row < self._num_teams + 2:
            self.insert_team_row(self._bottom_frame, temp_row, self._num_rounds)
            temp_row += 1
        self._main_window.add(self._bottom_frame, weight=1)

        # Status Bar
        status_frame = ttk.Frame(self._main_window, width=600, height=15, padding=5, relief=RIDGE)
        app_name_label = ttk.Label(status_frame, text='Pub Trivia App {0}'.format(self._version))
        app_name_label.config(foreground='#999999')
        app_name_label.pack(fill=X, side=LEFT)
        date_label = ttk.Label(status_frame, text=datetime.date.today())
        date_label.config(foreground='#999999')
        date_label.pack(fill=X, side=RIGHT)
        self._main_window.add(status_frame, weight=0)

    def insert_team_row(self, frame, index, num_rounds):
        row_frame = ttk.Frame(frame, padding=1, relief=FLAT)
        ttk.Label(row_frame, width=1, text=str(index)).pack(fill=X, expand=True, side=LEFT)
        ttk.Entry(row_frame, width=25).pack(fill=X, expand=True, side=LEFT)
        for i in range(1, num_rounds + 1):
            field = ttk.Entry(row_frame, width=10)
            field.bind('<FocusOut>', self.sum_rounds(index))
            field.pack(fill=X, expand=True, side=LEFT)
        ttk.Entry(row_frame, width=10).pack(fill=X, expand=True, side=LEFT)
        row_frame.pack(fill=X)
        Grid.rowconfigure(frame, index, weight=1)

    def add_team_click(self):
        self._num_teams += 1
        self.insert_team_row(self._bottom_frame, self._num_teams+1, self._num_rounds)

    def remove_team_click(self):
        self._num_teams -= 1

    def sum_rounds(self, row_index):
        pass


def main():
    # class testing goes here
    pass

if __name__ == '__main__':
    main()
