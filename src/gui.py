import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from src.base_classes import Machine, PoweredDevice, SpecializedFunction

class RobotGarageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Garage - Build Your Custom Robot")
        self.root.geometry("650x600")
        self.root.configure(bg="#1e1e1e")

        # Header Label
        self.header_label = tk.Label(
            root, text="Robot Garage", font=("Arial", 20, "bold"), fg="white", bg="#1e1e1e"
        )
        self.header_label.pack(pady=15)

        # Dropdown selections
        self.selection_frame = tk.Frame(root, bg="#1e1e1e")
        self.selection_frame.pack(pady=10)

        self.machine_label = tk.Label(self.selection_frame, text="Select Robot Type:", fg="white", bg="#1e1e1e")
        self.machine_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.machine_var = tk.StringVar()
        self.machine_dropdown = ttk.Combobox(self.selection_frame, textvariable=self.machine_var, values=["Drone", "Humanoid", "Quadruped"], state="readonly")
        self.machine_dropdown.grid(row=0, column=1, padx=5, pady=5)
        self.machine_dropdown.bind("<<ComboboxSelected>>", self.update_robot_image)

        self.power_label = tk.Label(self.selection_frame, text="Select Power Source:", fg="white", bg="#1e1e1e")
        self.power_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.power_var = tk.StringVar()
        self.power_dropdown = ttk.Combobox(self.selection_frame, textvariable=self.power_var, values=["Electric", "Solar", "Hybrid"], state="readonly")
        self.power_dropdown.grid(row=1, column=1, padx=5, pady=5)
        self.power_dropdown.bind("<<ComboboxSelected>>", self.update_robot_image)

        self.function_label = tk.Label(self.selection_frame, text="Select Functionality:", fg="white", bg="#1e1e1e")
        self.function_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.function_var = tk.StringVar()
        self.function_dropdown = ttk.Combobox(self.selection_frame, textvariable=self.function_var, values=["AI Assistant", "Heavy Lifter", "Security"], state="readonly")
        self.function_dropdown.grid(row=2, column=1, padx=5, pady=5)
        self.function_dropdown.bind("<<ComboboxSelected>>", self.update_robot_image)

        # Buttons
        self.button_frame = tk.Frame(root, bg="#1e1e1e")
        self.button_frame.pack(pady=15)

        self.build_button = tk.Button(
            self.button_frame, text="Build Robot", font=("Arial", 12, "bold"), fg="white", bg="#4CAF50",
            command=self.build_robot
        )
        self.build_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(
            self.button_frame, text="Clear", font=("Arial", 12, "bold"), fg="white", bg="#FF5733",
            command=self.clear_selections
        )
        self.clear_button.pack(side=tk.LEFT, padx=10)

        # Display area
        self.display_frame = tk.Frame(root, bg="#252525", bd=2, relief=tk.SUNKEN)
        self.display_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        self.image_labels = {}
        for label in ["machine", "power", "function"]:
            self.image_labels[label] = tk.Label(self.display_frame, bg="#252525")
            self.image_labels[label].pack(side=tk.LEFT, padx=20, anchor="center")

        self.description_label = tk.Label(
            root, text="", font=("Arial", 12), fg="white", bg="#1e1e1e", wraplength=600, justify="center"
        )
        self.description_label.pack(pady=10)

    def build_robot(self):
        robot_type = self.machine_var.get()
        power_type = self.power_var.get()
        function_type = self.function_var.get()

        if not (robot_type and power_type and function_type):
            self.description_label.config(text="Please select all options to build your robot.")
            return

        robot = Machine(robot_type)
        power = PoweredDevice(power_type)
        function = SpecializedFunction(function_type)

        robot_description = f"Your {robot.get_type()} runs on {power.get_power_source()} and specializes in {function.get_function_description()}."
        self.description_label.config(text=robot_description)
        self.update_robot_image()

    def update_robot_image(self, event=None):
        selections = {
            "machine": self.machine_var.get(),
            "power": self.power_var.get(),
            "function": self.function_var.get()
        }

        image_paths = {
            "Drone": "images/drone.png",
            "Humanoid": "images/humanoid.png",
            "Quadruped": "images/quadruped.png",
            "Electric": "images/electric.png",
            "Solar": "images/solar.png",
            "Hybrid": "images/hybrid.png",
            "AI Assistant": "images/ai_assistant.png",
            "Heavy Lifter": "images/heavy_lifter.png",
            "Security": "images/security.png"
        }

        for category, selection in selections.items():
            if selection in image_paths:
                img = Image.open(image_paths[selection]).resize((100, 100))
                self.image_labels[category].img = ImageTk.PhotoImage(img)
                self.image_labels[category].config(image=self.image_labels[category].img)

    def clear_selections(self):
        self.machine_var.set("")
        self.power_var.set("")
        self.function_var.set("")
        self.description_label.config(text="")
        for label in self.image_labels.values():
            label.config(image="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotGarageApp(root)
    root.mainloop()
