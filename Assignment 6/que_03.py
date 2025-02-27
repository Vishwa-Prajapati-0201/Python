# Write a class called Converter. The user will pass a length and a unit when declaring an object
# from the class—for example, c = Converter(9,'inches'). The possible units are inches, feet,
# yards, miles, kilometers, meters, centimeters, and millimeters. For each of these units there
# should be a method that returns the length converted into those units. For example, using the
# Converter object created above, the user could call c.feet() and should get 0.75 as the result.

class Converter:
    # Conversion factors to meters
    conversion_factors = {
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144,
        "miles": 1609.34,
        "kilometers": 1000,
        "meters": 1,
        "centimeters": 0.01,
        "millimeters": 0.001
    }

    def __init__(self, length, unit):
        if unit not in self.conversion_factors:
            raise ValueError("Invalid unit. Supported units: " + ", ".join(self.conversion_factors.keys()))
        self.length_in_meters = length * self.conversion_factors[unit]  # Convert input to meters

    def convert_to(self, target_unit):
        """Converts length to the given unit."""
        if target_unit not in self.conversion_factors:
            raise ValueError("Invalid target unit. Supported units: " + ", ".join(self.conversion_factors.keys()))
        return self.length_in_meters / self.conversion_factors[target_unit]