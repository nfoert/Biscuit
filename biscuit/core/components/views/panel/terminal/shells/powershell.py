import os

from biscuit.core.components.utils import Label

from ..terminal import Terminal


class PowerShell(Terminal):
    """
    PowerShell - Checks for powershell executable in path and opens that in terminal. 
    Shows Not Available in case variable is not set.

    """
    shell = "powershell"
    name = "PowerShell"
    icon = "powershell"
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

        if not self.shell:
            Label(self, text="PowerShell not available, report an issue otherwise.").grid()
            self.name = "Not Available"
            self.icon = "error"
            return
        
        self.start_service()
