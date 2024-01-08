class Booking():
    def __init__(self, seat):
        self.seat = seat
        self.customers = []

    def add_customer(self, name):
        if not self.open_seats():
            return False
        self.customers.append(name)
        return True

    def open_seats(self):
        return self.seat - len(self.customers)


booking = Booking(5)

guest = ["Neil", "Marry", "Jason", "Michael", "Lee", "James"]
for individual in guest:
    ADDED = booking.add_customer(individual)
    if ADDED:
        print(f"Added {individual} to booking list sucessfully")
    else:
        print(f"No available seats for {individual}")
