import Items, Employees, Grocery_Store, Timeclock, Shoppers, Transaction

cm = Grocery_Store.Grocery_Store('Central Market')
cm.store_address = '123 Market Street'
cm.store_number = 8325148237
sb = Shoppers.Shoppers('Sally')
sb.address = '7200 Preston'
sb.phone_number = 2814242640
sb.loyalty_number = 1234
gg = Employees.Employees('Gregory Garcia')
gg.ID_number = 210
gg.address = '7200 Preston'
gg.salary = 20
gg.hours = 80

pancakes = Items.Items('Pancake Mix')
pancakes.barcode = 892392
pancakes.brand = 'Stonewall Kitchen'
pancakes.category = 'Dry Goods'
pancakes.price = 2.99

bacon = Items.Items('Applewood Smoked Bacon')
bacon.barcode = 938349
bacon.brand = 'HEB'
bacon.category = 'Meat'
bacon.price = 4.99

syrup = Items.Items('Maple Syrup')
syrup.barcode = 123987
syrup.brand = "Doodle's Sugarbush"
syrup.category = 'Condiments'
syrup.price = 1.99

transaction = Transaction.Transaction('Name')
transaction.set_date()
transaction.scan_item(pancakes)
transaction.scan_item(bacon)
transaction.scan_item(syrup)
transaction.total_cost()

cm.print_receipt(sb, transaction)
