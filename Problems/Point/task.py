class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** (1 / 2)
