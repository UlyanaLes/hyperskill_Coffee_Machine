class Painting:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the Louvre.')


new_painting = Painting(input(), input(), input())
