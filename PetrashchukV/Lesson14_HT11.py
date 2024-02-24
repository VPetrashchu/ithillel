class ArtObject:
    def __init__(self, title, creator, year):
        self._title = title
        self._creator = creator
        self._year = year

    @property
    def title(self):
        return self._title

    @property
    def creator(self):
        return self._creator

    @property
    def year(self):
        return self._year

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @creator.setter
    def creator(self, new_creator):
        self._creator = new_creator

    @year.setter
    def year(self, new_year):
        self._year = new_year

    def show_info(self):
        raise NotImplementedError("Subclasses should implement this method")


class Painting(ArtObject):
    def __init__(self, title, creator, year, style):
        super().__init__(title, creator, year)
        self._style = style

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, new_style):
        self._style = new_style

    def show_info(self):
        print(f"Title: {self.title}\nCreator: {self.creator}\nYear: {self.year}\nStyle: {self.style}")


class Sculpture(ArtObject):
    def __init__(self, title, creator, year, material):
        super().__init__(title, creator, year)
        self._material = material

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, new_material):
        self._material = new_material

    def show_info(self):
        print(f"Title: {self.title}\nCreator: {self.creator}\nYear: {self.year}\nMaterial: {self.material}")


painting = Painting("Starry Night", "Vincent van Gogh", 1889, "Post-Impressionism")
sculpture = Sculpture("David", "Michelangelo", 1504, "Marble")

print("Painting Information:")
painting.show_info()
print("\nSculpture Information:")
sculpture.show_info()

painting.title = "The Starry Night"
sculpture.year = 1501

print("\nUpdated Painting Information:")
painting.show_info()
print("\nUpdated Sculpture Information:")
sculpture.show_info()
