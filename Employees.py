from unicodedata import name


class Employees:
    name = ''        # string
    ID_number = 0    # int
    address = ''     # string
    salary = 0       # float
    hours = 0        # float

    def __init__(self, name):
        self.name = name