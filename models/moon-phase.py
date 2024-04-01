import datetime
import math
from astral import LocationInfo, moon, geocoder

class MoonData:
    def __init__(self, city_name, dt):
        self.city_name = city_name
        self.dt = dt
        self.location = self._get_location_info(city_name)
    
    def _get_location_info(self, city_name):
        # Use the geocoder to look up the city
        return geocoder.lookup(city_name, geocoder.database())
    
    def _moonrise(self):
        # print(self.dt)
        # print(self.location)
        city = LocationInfo("London", "England", "Europe/London", 51.5, -0.116)
        # print(city)
        rise = moon.moonrise(self.location.observer, self.dt, self.location.timezone)
        # print(rise)
        return moon.moonrise(self.location.observer, self.dt)

    def _moonset(self):
        return moon.moonset(self.location.observer, self.dt)

    def _moon_phase(self):
        return moon.phase(self.dt)
    
    def _moon_illumination(self):
        # Convert phase to a fraction of the Moon's cycle
        phase = self._moon_phase()
        cycle_fraction = phase / 29.5
        # Calculate illumination using a sine function
        illumination = 0.5 * (1 + math.cos(2 * math.pi * (cycle_fraction - 0.5)))
        return illumination

    def get_moon_data(self):
        return {
            "moonrise": self._moonrise().isoformat(),
            "moonset": self._moonset().isoformat(),
            "moon_phase": self._moon_phase(),
            "moon_illumination": self._moon_illumination()
        }

dt = datetime.date(2024, 4, 8)
moon_phase_instance = MoonData("Los Angeles", dt)
moon_data = moon_phase_instance.get_moon_data();
print(moon_data)