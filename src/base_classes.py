# base_classes.py - Defines the fundamental classes for the Robot Garage

class Machine:
    """
    Represents a general machine. 
    This is the broadest category, meaning all robots are machines.
    """
    def __init__(self, type_name="General Machine"):
        self.type = type_name
    
    def get_type(self):
        return f"Type: {self.type}"
    
    def get_type_description(self):
        descriptions = {
            "Drone": "A lightweight flying robot, commonly used for surveillance and deliveries.\n",
            "Humanoid": "A robot designed to resemble a human, used for AI interactions and assistance.\n",
            "Quadruped": "A four-legged robot, often used for terrain exploration and heavy-duty tasks.\n"
        }
        return f"{self.type}: {descriptions.get(self.type, 'Unknown machine type.')}"

class PoweredDevice:

    def __init__(self, power_source):
        self.power_source = power_source
    
    def get_power_source(self):
        return f"Power Source: {self.power_source}"
    
    def get_power_description(self):
        descriptions = {
            "Electric": "Fast charging but consumes a lot of energy.\n",
            "Solar": "Eco-friendly but only works efficiently in daylight.\n",
            "Hybrid": "A balance between efficiency and power usage.\n"
        }
        return f"{self.power_source}: {descriptions.get(self.power_source, 'Unknown power source.')}"

class SpecializedFunction:

    def __init__(self, function):
        self.function = function
    
    def get_function(self):
        return f"Specialty: {self.function}"

    def get_function_description(self):
        descriptions = {
            "AI Assistant": "This robot is designed for intelligent interactions, capable of learning and adapting.",
            "Heavy Lifter": "Built for strength, this robot is ideal for carrying heavy loads.",
            "Security": "Equipped with sensors and monitoring tools, this robot ensures safety and surveillance."
        }
        return f"{self.function}: {descriptions.get(self.function, 'Unknown specialty.')}"
