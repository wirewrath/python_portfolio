class Phone:
    def __init__(self, battery_level):
        self.battery_level = battery_level
    def charge(self, amount):
        self.battery_level += amount
        if self.battery_level >100:
            self.battery_level = 100
        if self.battery_level < 0:
            self.battery_level = 0

my_phone = Phone(90)
my_phone.charge(20)
print(my_phone.battery_level)