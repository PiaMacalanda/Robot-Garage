import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from src.base_classes import Machine, PoweredDevice, SpecializedFunction
from src.robot import CustomizedRobot

class RobotGarageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Garage - Build Your Custom Robot")
        self.root.geometry("800x750")
        self.root.configure(bg="#1e1e1e")
        
        # Set custom style for widgets
        self.setup_styles()
        
        # Create main container
        self.main_container = tk.Frame(root, bg="#1e1e1e")
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Split into left panel (controls) and right panel (preview)
        self.left_panel = tk.Frame(self.main_container, bg="#1e1e1e")
        self.right_panel = tk.Frame(self.main_container, bg="#252525", bd=2, relief=tk.GROOVE)
        
        self.left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Header with app name and tagline
        self.create_header()
        
        # Selection area
        self.create_selection_area()
        
        # Preview area title
        self.preview_title = tk.Label(
            self.right_panel, 
            text="Robot Preview", 
            font=("Arial", 14, "bold"), 
            fg="white", 
            bg="#252525"
        )
        self.preview_title.pack(pady=(15, 5))
        
        # Robot preview image container
        self.preview_frame = tk.Frame(self.right_panel, bg="#252525")
        self.preview_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Robot image display
        self.robot_display = tk.Label(self.preview_frame, bg="#252525")
        self.robot_display.pack(pady=10)
        
        # Component images display
        self.components_frame = tk.Frame(self.preview_frame, bg="#252525")
        self.components_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.image_labels = {}
        component_titles = {"machine": "Robot Type", "power": "Power Source", "function": "Functionality"}
        
        for i, (key, title) in enumerate(component_titles.items()):
            component_frame = tk.Frame(self.components_frame, bg="#252525")
            component_frame.grid(row=0, column=i, padx=10, pady=5)
            
            title_label = tk.Label(component_frame, text=title, font=("Arial", 10), fg="#cccccc", bg="#252525")
            title_label.pack(pady=(0, 5))
            
            self.image_labels[key] = tk.Label(component_frame, bg="#252525", width=50, height=50)
            self.image_labels[key].pack()
        
        # Description area
        self.description_frame = tk.Frame(self.right_panel, bg="#303030", bd=1, relief=tk.SUNKEN)
        self.description_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.description_title = tk.Label(
            self.description_frame, 
            text="Robot Specifications", 
            font=("Arial", 12, "bold"), 
            fg="white", 
            bg="#303030"
        )
        self.description_title.pack(pady=(5, 0))
        
        self.description_label = tk.Label(
            self.description_frame, 
            text="Select components to see specifications", 
            font=("Arial", 10), 
            fg="#cccccc", 
            bg="#303030", 
            wraplength=400, 
            justify="center"
        )
        self.description_label.pack(pady=10)
        
        # Add inheritance explanation section
        self.add_inheritance_explanation()
        
        # Status bar
        self.status_bar = tk.Label(
            root, 
            text="Ready to build your robot", 
            bd=1, 
            relief=tk.SUNKEN, 
            anchor=tk.W, 
            bg="#303030", 
            fg="#cccccc"
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Initialize cached images dictionary
        self.cached_images = {}
        
        # Default placeholder image
        self.placeholder_img = self.load_and_resize_image("images/placeholder.png", (150, 150))
        if not self.placeholder_img:
            # Create a placeholder if image not found
            self.placeholder_img = self.create_placeholder_image((150, 150))
            
    def setup_styles(self):
        """Configure custom ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Combobox style
        style.configure('TCombobox', 
                        fieldbackground="#303030", 
                        background="#303030", 
                        foreground="white", 
                        arrowcolor="white")
        
        style.map('TCombobox', 
                 fieldbackground=[('readonly', '#303030')],
                 selectbackground=[('readonly', '#505050')],
                 selectforeground=[('readonly', 'white')])
        
    def create_header(self):
        """Create header area with logo and title"""
        header_frame = tk.Frame(self.left_panel, bg="#1e1e1e")
        header_frame.pack(fill=tk.X, pady=(0, 15))
        
        # App title
        self.header_label = tk.Label(
            header_frame, 
            text="Robot Garage", 
            font=("Arial", 20, "bold"), 
            fg="#4CAF50", 
            bg="#1e1e1e"
        )
        self.header_label.pack(pady=(15, 0))
        
        # Tagline
        self.tagline_label = tk.Label(
            header_frame, 
            text="OOP Inheritance Demo", 
            font=("Arial", 12, "italic"), 
            fg="#cccccc", 
            bg="#1e1e1e"
        )
        self.tagline_label.pack(pady=(0, 10))
        
    def create_selection_area(self):
        """Create the selection area with dropdowns and buttons"""
        # Selection frame with title
        selection_title = tk.Label(
            self.left_panel, 
            text="Robot Configuration", 
            font=("Arial", 14, "bold"), 
            fg="white", 
            bg="#1e1e1e"
        )
        selection_title.pack(anchor="w", pady=(0, 10))
        
        # Dropdowns container with nice spacing
        self.selection_frame = tk.Frame(self.left_panel, bg="#1e1e1e")
        self.selection_frame.pack(fill=tk.X, pady=5)
        
        # Robot Type selection
        self.machine_label = tk.Label(
            self.selection_frame, 
            text="Robot Type:", 
            font=("Arial", 11), 
            fg="white", 
            bg="#1e1e1e"
        )
        self.machine_label.grid(row=0, column=0, padx=5, pady=8, sticky="w")
        
        self.machine_var = tk.StringVar()
        self.machine_dropdown = ttk.Combobox(
            self.selection_frame, 
            textvariable=self.machine_var, 
            values=["Drone", "Humanoid", "Quadruped"], 
            state="readonly",
            width=15
        )
        self.machine_dropdown.grid(row=0, column=1, padx=5, pady=8, sticky="w")
        self.machine_dropdown.bind("<<ComboboxSelected>>", self.update_preview)
        
        # Power Source selection
        self.power_label = tk.Label(
            self.selection_frame, 
            text="Power Source:", 
            font=("Arial", 11), 
            fg="white", 
            bg="#1e1e1e"
        )
        self.power_label.grid(row=1, column=0, padx=5, pady=8, sticky="w")
        
        self.power_var = tk.StringVar()
        self.power_dropdown = ttk.Combobox(
            self.selection_frame, 
            textvariable=self.power_var, 
            values=["Electric", "Solar", "Hybrid"], 
            state="readonly",
            width=15
        )
        self.power_dropdown.grid(row=1, column=1, padx=5, pady=8, sticky="w")
        self.power_dropdown.bind("<<ComboboxSelected>>", self.update_preview)
        
        # Functionality selection
        self.function_label = tk.Label(
            self.selection_frame, 
            text="Functionality:", 
            font=("Arial", 11), 
            fg="white", 
            bg="#1e1e1e"
        )
        self.function_label.grid(row=2, column=0, padx=5, pady=8, sticky="w")
        
        self.function_var = tk.StringVar()
        self.function_dropdown = ttk.Combobox(
            self.selection_frame, 
            textvariable=self.function_var, 
            values=["AI Assistant", "Heavy Lifter", "Security"], 
            state="readonly",
            width=15
        )
        self.function_dropdown.grid(row=2, column=1, padx=5, pady=8, sticky="w")
        self.function_dropdown.bind("<<ComboboxSelected>>", self.update_preview)
        
        # Spacer
        spacer = tk.Frame(self.left_panel, height=20, bg="#1e1e1e")
        spacer.pack(fill=tk.X)
        
        # Buttons with improved styling
        self.button_frame = tk.Frame(self.left_panel, bg="#1e1e1e")
        self.button_frame.pack(fill=tk.X, pady=10)
        
        self.build_button = tk.Button(
            self.button_frame, 
            text="Build Robot", 
            font=("Arial", 12, "bold"), 
            fg="white", 
            bg="#4CAF50",
            activebackground="#45a049",
            activeforeground="white",
            bd=0,
            padx=15,
            pady=8,
            command=self.build_robot
        )
        self.build_button.pack(fill=tk.X, pady=(0, 5))
        
        self.clear_button = tk.Button(
            self.button_frame, 
            text="Clear", 
            font=("Arial", 11), 
            fg="white", 
            bg="#555555",
            activebackground="#444444",
            activeforeground="white",
            bd=0,
            padx=15,
            pady=5,
            command=self.clear_selections
        )
        self.clear_button.pack(fill=tk.X)
        
    def add_inheritance_explanation(self):
        """Add a section explaining OOP inheritance"""
        inheritance_frame = tk.Frame(self.left_panel, bg="#252525", bd=1, relief=tk.GROOVE)
        inheritance_frame.pack(fill=tk.X, pady=(20, 0))
        
        inheritance_title = tk.Label(
            inheritance_frame,
            text="OOP Inheritance Demo",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#252525"
        )
        inheritance_title.pack(pady=(10, 5))
        
        inheritance_text = """
This application demonstrates Object-Oriented Programming inheritance:

• Machine (base class)
  ↓
• PoweredDevice (functionality)
  ↓
• SpecializedFunction (functionality)
  ↓
• CustomizedRobot (inherits all three)

When you build a robot, a CustomizedRobot object is created that inherits properties and methods from all parent classes.
        """
        
        explanation = tk.Label(
            inheritance_frame,
            text=inheritance_text,
            font=("Arial", 9),
            fg="#cccccc",
            bg="#252525",
            justify=tk.LEFT,
            wraplength=250,
            padx=10
        )
        explanation.pack(pady=(0, 10))
            
    def load_and_resize_image(self, path, size):
        """Load an image, resize it, and return a PhotoImage"""
        try:
            img = Image.open(path).resize(size)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image {path}: {e}")
            return None
            
    def create_placeholder_image(self, size):
        """Create a placeholder image with given size"""
        img = Image.new('RGB', size, color='#303030')
        return ImageTk.PhotoImage(img)
    
    def update_preview(self, event=None):
        """Update robot preview and component images"""
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
        
        # Update component images
        for category, selection in selections.items():
            if selection:
                if selection in image_paths:
                    path = image_paths[selection]
                    
                    # Use cached image if available, otherwise load and cache
                    if path not in self.cached_images:
                        self.cached_images[path] = self.load_and_resize_image(path, (250, 250))
                    
                    img = self.cached_images[path]
                    if img:
                        self.image_labels[category].config(image=img)
                    else:
                        self.image_labels[category].config(image="")
            else:
                self.image_labels[category].config(image="")
                
        # Update main robot preview
        robot_type = self.machine_var.get()
        if robot_type and robot_type in image_paths:
            path = image_paths[robot_type]
            if path not in self.cached_images:
                self.cached_images[path] = self.load_and_resize_image(path, (250, 250))
            
            img = self.cached_images[path]
            if img:
                self.robot_display.config(image=img)
            else:
                self.robot_display.config(image=self.placeholder_img)
        else:
            self.robot_display.config(image=self.placeholder_img)
            
        # Update description
        self.update_description()
    
    def update_description(self):
        """Update the robot description based on selections"""
        robot_type = self.machine_var.get()
        power_type = self.power_var.get()
        function_type = self.function_var.get()
        
        description = ""
        
        if robot_type:
            machine = Machine(robot_type)
            description += machine.get_type_description()
            
        if power_type:
            power = PoweredDevice(power_type)
            description += power.get_power_description()
            
        if function_type:
            function = SpecializedFunction(function_type)
            description += function.get_function_description()
            
        if not description:
            description = "Select components to see specifications"
            
        self.description_label.config(text=description)
        
    def build_robot(self):
        """Create a CustomizedRobot instance with selected components"""
        robot_type = self.machine_var.get()
        power_type = self.power_var.get()
        function_type = self.function_var.get()
        
        if not (robot_type and power_type and function_type):
            messagebox.showwarning("Missing Components", "Please select all components to build your robot.")
            self.status_bar.config(text="Error: Missing components")
            return
            
        # Create a CustomizedRobot object (demonstrates multiple inheritance)
        robot = CustomizedRobot(robot_type, power_type, function_type)
        
        # Get information using inherited methods
        robot_info = robot.get_robot_info()
        
        # Create a detailed description that shows inheritance in action
        description = f"Robot successfully built using OOP inheritance!\n\n"
        description += f"{robot_info}\n\n"
        description += f"This robot combines properties from:\n"
        description += f"• Machine class (type: {robot_type})\n"
        description += f"• PoweredDevice class (power: {power_type})\n"
        description += f"• SpecializedFunction class (function: {function_type})"
        
        self.description_label.config(text=description)
        self.status_bar.config(text=f"Robot built: CustomizedRobot instance created with multiple inheritance")
        
        # Show inheritance message
        messagebox.showinfo("OOP Inheritance Demo", 
                           f"A CustomizedRobot object has been created that inherits from all three parent classes!")
        
    def clear_selections(self):
        """Clear all selections and reset the interface"""
        self.machine_var.set("")
        self.power_var.set("")
        self.function_var.set("")
        
        # Clear images
        self.robot_display.config(image=self.placeholder_img)
        for label in self.image_labels.values():
            label.config(image="")
            
        # Reset description
        self.description_label.config(text="Select components to see specifications")
        self.status_bar.config(text="Ready to build your robot")

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotGarageApp(root)
    root.mainloop()