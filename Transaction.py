class Transaction:
    name = ''           # string
    total = 0           # int
    date = ''           # string
    list_of_items = []  # array

    def __init__(self, name):
        self.name = name

    def scan_item(self, item):
        self.list_of_items.append(item)
    
    def total_cost(self):
        for item in self.list_of_items:
            self.total += item.price
    
    def set_date(self):
        self.date = '3/4/22'