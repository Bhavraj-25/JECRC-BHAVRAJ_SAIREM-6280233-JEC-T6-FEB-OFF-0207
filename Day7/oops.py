class Car:
    ## contains varibles, methods
    wheels = 4
    engine = 'vi'
    base_speed = '40kmph'
    max_speed = '180kmph'
    gears = '5'
    suspension = 'independent'

    ## Constructor (__init__)
    '''
    class class_name:
        def __init__(self, arg1, arg2, arg3......argn):
            self.arg1 = arg1
            self.arg2 = arg2
            self.arg3 = arg3
    '''

    def __init__(self, air_bags, chassis, service):
        self.air_bags = air_bags
        self.chassis = chassis
        self.service = service

    def display(self):
        print(f'wheels: {self.wheels} \t engine: {self.engine} \t base_speed: {self.base_speed} \t max_speed: {self. max_speed} \t gears: {self.gears}')

    def update_speed(self, new_speed):
        self.base_speed = new_speed
        print(f'updated speed to: {self.base_speed}')
    
    def max_update(self, new_speed):
        self.max_speed = new_speed
        print(f'new max speed: {self.max_speed}')

    @classmethod
    def update_gears(cls, new_gear):
        cls.gears = new_gear
        print(f'gear updated: {cls.gears}')


TATA = Car()
print(TATA) ## print object memory location (hexadecimal)
TATA.suspension = 'dependent' # changing prop of existing prop
TATA.chassis_level = 'high' # new prop which belongs only to TATA obj

## for accessing properties/methods:
print(f'No. of wheelers: {TATA.wheels}')
print(f'Engine type: {TATA.engine}')
print(f'chassis type: {TATA.chassis_level}')

mahindra = Car()
print(mahindra)
print(f'No. of wheelers: {mahindra.wheels}')
print(f'Engine type: {mahindra.engine}')
print(f'Suspension type: {mahindra.suspension}')

suzuki = Car()
print(suzuki)
print(f'No. of wheelers: {suzuki.wheels}')
print(f'Engine type: {suzuki.engine}')
print(f'Suspension type: {suzuki.suspension}')

toyota = Car(air_bags=True, chassis='Medium', service='Very good')

## Can only set what is specified as args in __init__
# hyundai = Car(engine = ['vi','diesel','EV'], air_bags=True, chassis='Medium', service='OK', max_speed = '200kmph')
hyundai = Car(air_bags=True, chassis='Medium', service='OK')
hyundai.engine = ['vi','diesel','EV']
# print((hyundai.engine, hyundai.air_bags, hyundai.chassis, hyundai.service))
hyundai.update_speed('240kmph')
hyundai.max_update('320kmph')
hyundai.update_gears(8)
hyundai.display()


## Another way of passing args (should be in order)
suzuki = Car(True, 'poor', 'poor')