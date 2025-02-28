import sys
import os
import tkinter as tk
from src.gui import RobotGarageApp

# Ensure Python can find src directory
sys.path.append(os.path.abspath("src"))

root = tk.Tk()
app = RobotGarageApp(root)
root.mainloop()
