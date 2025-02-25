"""
Content container of the app
    .
    App
    └── Root
        ├── Menubar
        ├── BaseFrame
        │    ├── SideBar
        │    └── ContentPane 
        │        ├── EditorsPane
        │        └── Panel
        └── StatusBar
"""
from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .. import BaseFrame

import tkinter as tk

from biscuit.core.components.utils import Frame

from .editors import EditorsPane
from .panel import Panel


class ContentPane(Frame):
    """
    Main frame holds ContentPane and Panel
    """
    def __init__(self, master: BaseFrame, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.config(bg=self.base.theme.border)
        
        self.editorspane = EditorsPane(self)
        self.panel = Panel(self)
        self._panel_enabled = False
        self._panel_maxed = False

        self.editorspane.pack(fill=tk.BOTH, expand=True)
    
    def show_panel(self) -> None:
        if not self._panel_enabled:
            self.toggle_panel()
    
    def toggle_panel(self, *_) -> None:
        if self._panel_enabled:
            self.panel.pack_forget()
            self.editorspane.pack(fill=tk.BOTH, expand=True)
        else:
            if self._panel_maxed:
                self.panel.pack(fill=tk.BOTH, pady=(1, 0), expand=True)
                self.editorspane.pack_forget()
            else:
                self.panel.pack(fill=tk.BOTH, pady=(1, 0))

        self._panel_enabled = not self._panel_enabled
    
    def toggle_max_panel(self, *_) -> None:
        if self._panel_maxed:
            self.panel.pack_forget()
            self.editorspane.pack(fill=tk.BOTH, expand=True)
            self.panel.pack(fill=tk.BOTH, pady=(1, 0))
        else:
            self.editorspane.pack_forget()
            self.panel.pack(fill=tk.BOTH, pady=(1, 0), expand=True)
        
        self._panel_maxed = not self._panel_maxed
