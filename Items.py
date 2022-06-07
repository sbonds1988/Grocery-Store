class Items:
    barcode = 0     # int
    brand = ''      # string
    category = ''   # string
    product = ''    # string
    price = 0       # float

    def __init__(self, name):
        self.product = name