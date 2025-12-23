class Theater:
    def __init__(self, id, name, location, capacity):
        self.id = id
        self.name = name
        self.location = location
        self.capacity = capacity
        self.seats = {
            "VIP": {"capacity": 5, "price": 20},
            "Standard": {"capacity": 15, "price": 15},
            "Economy": {"capacity": 10, "price": 10}
        }

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location
    
    def get_capacity(self):
        return int(self.capacity)
    
    def get_seat_types(self):
        return self.seats.keys()
    
    def get_seat_price(self, seat_type):
        return self.seats[seat_type]["price"]
    
    def get_seat_capacity(self, seat_type):
        return self.seats[seat_type]["capacity"]

