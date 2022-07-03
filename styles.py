import tkinter as tk


class EntryBlack(tk.Entry):
    def __init__(self, *args, **kwargs):
        if 'bg' not in kwargs:
            kwargs['bg'] = '#353535'
        if 'fg' not in kwargs:
            kwargs['fg'] = '#ffffff'
        if 'insertbackground' not in kwargs:
            kwargs['insertbackground'] = '#ffffff' 
        super(EntryBlack, self).__init__(*args, **kwargs)

tk.Entry = EntryBlack


class TkBlack(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(TkBlack, self).__init__(*args, **kwargs)
        self.configure(bg='#222222')

tk.Tk = TkBlack

class LabelBlack(tk.Label):
    def __init__(self, *args, **kwargs):
        if 'bg' not in kwargs:
            kwargs['bg'] = '#353535'
        if 'fg' not in kwargs:
            kwargs['fg'] = '#ffffff'
        super(LabelBlack, self).__init__(*args, **kwargs)

tk.Label = LabelBlack

class ButtonBlack(tk.Button):
    def __init__(self, *args, **kwargs):
        if 'bg' not in kwargs:
            kwargs['bg'] = '#353535'
        if 'fg' not in kwargs:
            kwargs['fg'] = '#ffffff'
        super(ButtonBlack, self).__init__(*args, **kwargs)

tk.Button = ButtonBlack


black_kwargs = {
    'bg': '#353535',
    'fg': '#ffffff',
    'insertbackground': '#ffffff'
}