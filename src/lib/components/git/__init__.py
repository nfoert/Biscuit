import tkinter as tk

from .core import GitCore
from .repo import GitRepo
from .tree import GitTree
from .utils.toolbar import GitTreeToolbar

from ..text import utils
from ..sidebar.pane import SidePane
from ..utils.scrollbar import AutoScrollbar
from ..placeholders.emptygittree import EmptyGitTree

class GitPane(SidePane):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.base = master.base

        self.name = "Source Control"
        self.icon = "💼"
        self.tree_active = False
        
        self.core = self.base.git

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.label_frame = tk.Frame(self)
        self.label_frame.config(bg="#E6E6E6")
        self.label_frame.grid(row=0, column=0, sticky=tk.EW)
        
        self.label = tk.Label(self.label_frame)
        self.label.config(
            text="SOURCE CONTROL", font=("Segoe UI", 10), anchor=tk.W, 
            bg="#E6E6E6", fg="#6f6f6f")
        self.label.grid(row=0, column=0, sticky=tk.EW, padx=25, pady=9)


        self.empty_tree = EmptyGitTree(self)
        self.empty_tree.grid(row=1, column=0, sticky=tk.NSEW, padx=25, pady=10)

        self.toolbar = GitTreeToolbar(self)
        self.toolbar.config(bg="#E6E6E6")

        self.tree = GitTree(self, selectmode=tk.BROWSE)
        self.tree_scrollbar = AutoScrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)

        self.tree.configure(yscrollcommand=self.tree_scrollbar.set)
        self.update_panes()
    
    def create_root(self):
        self.tree.open_repo_dir()
        self.toolbar.update()
    
    def disable_tree(self):
        if self.tree_active:
            self.toolbar.grid_remove()
            self.tree.grid_remove()
            self.tree_scrollbar.grid_remove()
            self.empty_tree.grid()
            self.tree_active = False
    
    def enable_tree(self):
        if not self.tree_active:
            self.empty_tree.grid_remove()
            self.toolbar.grid(row=1, column=0, sticky=tk.EW, padx=(25, 1))
            self.tree.grid(row=2, column=0, sticky=tk.NSEW)
            self.tree_scrollbar.grid(row=2, column=1, sticky=tk.NS)
            self.tree_active = True
    
    def update_panes(self):
        if self.base.active_dir is not None:
            self.enable_tree()
        else:
            self.disable_tree()
