
class Town:
    def __init__(self, name: str, latitude="", longitude=""):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


# town = Town("Sofia")
# town.set_latitude("42° 41\' 51.04\" N")
# town.set_longitude("23° 19\' 26.94\" E")
# print(town)
# town = Town("Varna")
# town.set_latitude("46° 41\' 53.04\" N")
# town.set_longitude("22° 41\' 34.04\" E")
# print(town)
