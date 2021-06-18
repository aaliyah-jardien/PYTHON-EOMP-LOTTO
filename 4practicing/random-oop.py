import random

class Bus:
    # This describes what the bus will look like

    def __init__(self, driver, num_of_color, num_of_seats):
        self.driver = driver
        self.num_of_color = num_of_color
        self.num_of_seats = num_of_seats

bus = Bus("Aaliyah", ["Red", "Blue", "Green", "Yellow", "Purple"], "80")

print(bus.driver)
print(bus.num_of_color[random.randint(0, 4)])
print(bus.num_of_seats)
