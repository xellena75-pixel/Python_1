class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __repr__(self):
        return f"{self.index}, {self.city}, {self.street}, дом {self.house}, кв. {self.apartment}"
