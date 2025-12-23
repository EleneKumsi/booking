class Booking:
    def __init__(self, name, movie_name, theater_name, date, time, tickets, total_price):
        self.name = name
        self.movie_name = movie_name
        self.theater_name = theater_name
        self.tickets = tickets
        self.date = date
        self.time = time
        self.total_price = total_price

    def get_name(self):
        return self.name
    
    def get_movie_name(self):
        return self.movie_name
    
    def get_theater_name(self):
        return self.theater_name
    
    def get_date(self):
        return self.date
    
    def get_time(self):
        return self.time
    
    def get_tickets(self):
        return self.tickets
    
    def get_total_price(self):
        return self.total_price