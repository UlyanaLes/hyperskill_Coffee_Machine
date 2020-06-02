class Alien:
    count = 0
    places = []

    def __init__(self, planet, species):
        self.planet = planet
        self.species = species


mart = Alien("Mars", "martian")
mart.places.append("Mars")
mart.count += 1

dalek = Alien("Scaro", "dalek")
dalek.places.append("Scaro")
dalek.count += 1

Alien.count += 2


print(Alien.count)
print(Alien.places)
print(mart.count)
print(mart.places)
print(dalek.count)
print(dalek.places)