"""
Base container of the app
    .
    App
    └── Root
        ├── Menubar
        ├── BaseFrame
        │    ├── Sidebar
        │    └── ContentPane 
        └── StatusBar
"""
from __future__ import annotations

import tkinter as tk
import typing

if typing.TYPE_CHECKING:
    from .. import Root

from biscuit.core.components.utils import Frame

from .content import ContentPane
from .sidebar import Sidebar


class BaseFrame(Frame):
    """
    Main frame holds Sidebar and ContentPane
    """
    def __init__(self, master: Root, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.config(bg=self.base.theme.border)

        self.sidebar = Sidebar(self)
        self.contentpane = ContentPane(master=self)

        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.contentpane.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
