class DeliveryRobot:
    battery_level = 25
    def request_charge_check(self):
        print("Robot is requesting a charge check")

class ChargingStation:
    name = "North Dock"
    def check_robot(self, robot):
        print(f"Station {self.name}: Robot batter level is {robot.battery_level}%")

robot1 = DeliveryRobot()
station1 = ChargingStation()

station1.check_robot(robot1)

class Museum:
    theme = "Ancient Egypt"

    def display_hours(self):
        print("Museum is open from 9 AM to 5 PM.")


class Guide:
    name = "Sarah"

    def give_tour(self, museum):
        print(f"Hi, I'm {self.name} and I will be guiding your tour of the {museum.theme} exhibit!")

museum1 = Museum()
guide1 = Guide()

museum1.display_hours()
guide1.give_tour(museum1)

class Phone:
    def __init__(self, battery):
        self.battery = battery

    def play_game(self):
        self.battery = self.battery - 10


my_phone = Phone(50)
my_phone.play_game()
my_phone.play_game()
print(my_phone.battery)

class Pet:
    species = "Dog"   # class attribute

    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age     # instance attribute

luna = Pet("Luna", 3)
rocky = Pet("Rocky", 5)

print(luna.name, luna.age, luna.species)
print(rocky.name, rocky.age, rocky.species)
luna.species = "Wolf"
print(luna.species)
print(rocky.species)
print(Pet.species)

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        print(self.name, "is a", self.species)


fluffy = Pet("Fluffy", "cat")
rex = Pet("Rex", "dog")
mittens = Pet("Mittens", "cat")

pets = [fluffy, rex, mittens]

for pet in pets:
    pet.describe()
for pet in pets:
    print("About to describe:", pet.name)
    pet.describe()
cat_count = 0

for pet in pets:
    if pet.species == "cat":
        cat_count = cat_count + 1

print(cat_count)

# Class definition


class Robot:
    """Represents a robot with energy levels and active status."""

    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.active = True

    def drain_energy(self, amount):
        """Drains energy from the robot and deactivates it if energy hits 0."""
        self.energy = self.energy - amount
        if self.energy <= 0:
            self.energy = 0
            self.active = False


# Main program

robots = [Robot("Alpha", 50), Robot("Beta", 20), Robot("Gamma", 10)]

for robot in robots:
    robot.drain_energy(25)

active_count = 0
for robot in robots:
    if robot.active:
        active_count = active_count + 1

print(f"{active_count} robots still active")

# Class definition


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Main program

count = int(input("How many pets? "))
pets = []

for i in range(count):
    name = input("Pet name: ")
    age = int(input("Pet age: "))
    pets.append(Pet(name, age))

for pet in pets:
    print(f"{pet.name} is {pet.age} years old")

class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 0

    def be_petted(self):
        print(self.name, "is being petted...")
        self.happiness += 10


class PetOwner:
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet

    def pet_the_pet(self):
        print(self.name, "is petting", self.pet.name)
        self.pet.be_petted()


# Demo
pet = Pet("Fluffy")
owner = PetOwner("Alice", pet)

print("Before petting, happiness:", pet.happiness)
owner.pet_the_pet()
print("After petting, happiness:", pet.happiness)