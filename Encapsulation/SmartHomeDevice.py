class SmartDevice:
    def __init__(self, battery_level):
        self.__is_on = False              
        self.__battery_level = battery_level  

    def turn_on(self):
        if self.__battery_level >= 20:
            self.__is_on = True
            print("Device is turned ON.")
        else:
            print("Battery too low to turn on the device.")

    def turn_off(self):
        self.__is_on = False
        print("Device is turned OFF.")

    @property
    def is_on(self):
        return self.__is_on

    @is_on.setter
    def is_on(self, value):
        if value:
            if self.__battery_level >= 20:
                self.__is_on = True
                print("Device turned ON via setter.")
            else:
                print("Cannot turn ON: Battery too low (setter).")
        else:
            self.__is_on = False
            print("Device turned OFF via setter.")

    @property
    def battery_level(self):
        return self.__battery_level

    @battery_level.setter
    def battery_level(self, value):
        if 0 <= value <= 100:
            self.__battery_level = value
        else:
            print("Battery level must be between 0 and 100.")
            
device = SmartDevice(battery_level=10)
device.turn_on()
device.is_on = True
device.battery_level = 50
device.turn_on()
device.is_on = False 
