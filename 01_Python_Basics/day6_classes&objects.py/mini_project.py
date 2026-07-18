class Planet:
    def __init__(self, name, planet_type, star):
        if type(name) != str or type(planet_type) != str or type(star) != str:
            raise TypeError("name, planet type, and star must be strings")

        if name == "" or planet_type == "" or star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


# Create three planet objects
planet_1=Planet("Earth", "Terrestrial", "Sun")
planet_2=Planet("Jupiter", "Gas Giant", "Sun")
planet_3=Planet("Mars", "Terrestrial", "Sun")

# Print the objects
print(planet_1)
print(planet_2)
print(planet_3)

# Print the orbit messages
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())