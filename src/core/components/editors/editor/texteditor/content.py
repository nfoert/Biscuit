import os
import tkinter as tk

<<<<<<< HEAD:src/core/components/editors/editor/texteditor/content.py
from .binder import Binder
=======
from .utils.binder import Binder
>>>>>>> dec37119ca8c68530b309efab68650a6ead758f5:src/core/components/editor_types/editor/content.py
from .linenumbers import LineNumbers

from ...text import Text
from ...utils import AutoScrollbar


class TextEditor(tk.Frame):
    def __init__(
        self, master, 
        path=None, exists=True, font=None, 
        *args, **kwargs
    ):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.path = path
        self.exists = exists
        self.font = font

        self.show_path = True
        self.editable = True
    
    def open_text_editor(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.text = Text(master=self, path=self.path, exists=self.exists)
        self.text.config(font=self.font)
        self.linenumbers = LineNumbers(master=self, text=self.text)

        self.scrollbar = AutoScrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.linenumbers.grid(row=0, column=0, sticky=tk.NS)
        self.text.grid(row=0, column=1, sticky=tk.NSEW)
        self.scrollbar.grid(row=0, column=2, sticky=tk.NS)

        if self.exists:
            self.text.load_file()

        self.binder = Binder(self)
        self.binder.bind_all()

    def unsupported_file(self):
        self.text.show_unsupported_dialog()
        self.linenumbers.grid_remove()
        self.scrollbar.grid_remove()
        self.editable = False
        self.base.root.statusbar.configure_editmode(False)

    def _on_change(self, event=None):
        self.linenumbers.redraw()
        self.base.update_statusbar_ln_col_info()
    
    def set_fontsize(self, size):
        self.font.configure(size=size)
        self.linenumbers.set_bar_width(size * 3)
        self._on_change()

    def cut(self, *_):
        if self.editable:
            self.text.cut()
    
    def copy(self, *_):
        if self.editable:
            self.text.copy()
        
    def paste(self, *_):
        if self.editable:
            self.text.paste()
