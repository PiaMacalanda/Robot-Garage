import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from src.robot import CustomizedRobot

class RobotGarageApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Build-a-Bot Workshop")
        self.master.geometry("500x400")

        # Title Label
        self.title_label = tk.Label(self.master, text="Customize Your Robot", font=("Arial", 14, "bold"))
        self.title_label.pack(pady=5)

        # Dropdowns for customization
        self.type_label = tk.Label(self.master, text="Select Robot Type:")
        self.type_label.pack()
        self.robot_type = ttk.Combobox(self.master, values=["Humanoid", "Quadruped", "Drone"], state="readonly")
        self.robot_type.pack()
        self.robot_type.bind("<<ComboboxSelected>>", self.update_image)

        self.power_label = tk.Label(self.master, text="Select Power Source:")
        self.power_label.pack()
        self.power_source = ttk.Combobox(self.master, values=["Electric", "Solar", "Hybrid"], state="readonly")
        self.power_source.pack()

        self.function_label = tk.Label(self.master, text="Select Specialty:")
        self.function_label.pack()
        self.function = ttk.Combobox(self.master, values=["AI Assistant", "Heavy Lifter", "Security"], state="readonly")
        self.function.pack()

        # Robot Image
        self.image_label = tk.Label(self.master)
        self.image_label.pack()

        # Submit Button
        self.create_button = tk.Button(self.master, text="Build Robot", command=self.create_robot, bg="green", fg="white")
        self.create_button.pack(pady=5)

        # Output Text
        self.output_text = tk.Text(self.master, height=5, width=50, state="disabled")
        self.output_text.pack()

        # Load images
        self.images = {
            "Humanoid": ImageTk.PhotoImage(Image.open("images/humanoid.png").resize((100, 100))),
            "Quadruped": ImageTk.PhotoImage(Image.open("images/quadruped.png").resize((100, 100))),
            "Drone": ImageTk.PhotoImage(Image.open("images/drone.png").resize((100, 100)))
        }

    def create_robot(self):
        selected_type = self.robot_type.get()
        selected_power = self.power_source.get()
        selected_function = self.function.get()
        
        if selected_type and selected_power and selected_function:
            robot = CustomizedRobot(selected_type, selected_power, selected_function)
            self.output_text.config(state="normal")
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, robot.get_robot_info())
            self.output_text.config(state="disabled")
        else:
            self.output_text.config(state="normal")
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Please select all options!")
            self.output_text.config(state="disabled")

    def update_image(self, event):
        selected_type = self.robot_type.get()
        if selected_type in self.images:
            self.image_label.config(image=self.images[selected_type])

