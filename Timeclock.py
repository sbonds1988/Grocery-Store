class Timeclock:
    def paycheck(emp):
        total_pay = emp.salary * emp.hours
        print("Pay to the order of:\n" + emp.name)
        print(emp.address)
        print("\nTotal Pay: " + str(total_pay))
    