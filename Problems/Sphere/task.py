class Sphere:
    PI = 3.1415

    def __init__(self, rad):
        self.radius = rad
        self.volume = 4 / 3 * Sphere.PI * self.radius ** 3
