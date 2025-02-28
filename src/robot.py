from src.base_classes import Machine, PoweredDevice, SpecializedFunction

class CustomizedRobot(Machine, PoweredDevice, SpecializedFunction):
    def __init__(self, robot_type, power_source, function):
        Machine.__init__(self)
        PoweredDevice.__init__(self, power_source)
        SpecializedFunction.__init__(self, function)
        self.type = robot_type  # Override general machine type

    def get_robot_info(self):
        return f"{self.get_type()}\n{self.get_power_source()}\n{self.get_function()}"
