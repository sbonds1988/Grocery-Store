class Grocery_Store:
    list_of_shoppers = []           # array
    list_of_items = []              # array of barcodes
    list_of_employees = []          # array
    list_of_receipts = []           # array
    list_of_timecards = []          # array
    store_name = ''                 # string
    store_address = ''              # string
    store_number = ''               # string
    scanned_items = []              # array

    def __init__(self, name):
        self.store_name = name

    def print_receipt(self, shopper, transaction):
        print(self.store_name)
        print(self.store_address)
        print(self.store_number)
        print(transaction.date)
        print(shopper.loyalty_number)
        for item in transaction.list_of_items:
            print(item.brand + " " + item.product + " " + str(item.price))
        print("Your total is: $" + str(transaction.total))