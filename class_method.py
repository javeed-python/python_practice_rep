class Vehicle:
    # define the class level attributes
    company = "Hyudai"
    fuel_type = "petrol"

    # initialize the instace atributes
    def __init__(self, **kwargs):
        # define atributes/properties
        self.name = kwargs['name']
        self.model = kwargs['model']
        self.type = kwargs['type']
        self.cost = kwargs['cost']

    # define class methods
    @classmethod
    def start(cls, integrated_app=False):
        if integrated_app:
            print(f'Your {cls.company} vehicle started with mobile app')
        else:
            print(f'Your {cls.company} vehicle started with Key manually')

    @classmethod
    def fill_fuel(cls, qty_ltrs):
        print(f'{cls.company} Vehicle got filled with {qty_ltrs} ltrs {cls.fuel_type}')

    # define instance method
    def show_details_pretty(self, **kwargs):
        vehicle_details = f'name:{self.name}\ncompany:{self.company}\ntype:{self.type}\ncost:{self.cost}'
        if kwargs:
            for name, value in kwargs.items():
                vehicle_details += f"\n{name}:{value}"

        print('vehicle details')
        print(vehicle_details)


car = Vehicle(name="Creta", company="Hyundai", model=2023,
              type="4 wheeler", cost=1545000, fuel_type="petrol")
car.show_details_pretty(wheels_type="Alloy", brakes="disk", sunroof="Yes", ADAS="Yes")
# car.fill_fuel(30)
# car.stvehicle details
# name:Creta
# company:Hyudai
# type:4 wheeler
# cost:1545000
# wheels_type:Alloy
# brakes:disk
# sunroof:Yes
# ADAS:Yes
# Hyudai Vehicle got filled with 30 ltrs petrol
# Your Hyudai vehicle started with Key manuallyart()
Vehicle.fill_fuel(30)
Vehicle.start()
