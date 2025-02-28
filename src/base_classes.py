class Machine:
    def __init__(self):
        self.type = "General Machine"

    def get_type(self):
        return f"Type: {self.type}"

class PoweredDevice:
    def __init__(self, power_source):
        self.power_source = power_source

    def get_power_source(self):
        return f"Power Source: {self.power_source}"

class SpecializedFunction:
    def __init__(self, function):
        self.function = function

    def get_function(self):
        return f"Specialty: {self.function}"
