class Movie:
    def __init__(self, id, title, director, year, duration, price):
        self.id = id
        self.title = title
        self.director = director
        self.year = int(year)
        self.duration = float(duration)
        self.price = float(price)

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title
    
    def get_director(self):
        return self.director
    
    def get_year(self):
        return self.year
    
    def get_duration(self):
        return self.duration
        
    def get_price(self):
        return float(self.price)