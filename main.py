from models.theater import Theater
from models.movie import Movie
from models.booking import Booking
import csv
import os
import matplotlib.pyplot as plt

theaters = []
movies = []
bookings = []
days = ["ორშაბათი", "სამშაბათი", "ოთხშაბათი", "ხუთშაბათი", "პარასკევი", "შაბათი", "კვირა"]
time = ["15:30", "17:00", "19:15", "22:30"]

with open('data/theater.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        theater = Theater(row['id'], row['name'], row['location'], row['capacity'])
        theaters.append(theater)

with open('data/movie.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie = Movie(row['id'], row['title'], row['director'], row['year'], row['duration'], row['price'])
        movies.append(movie)

with open('data/bookings.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        booking = Booking(row['name'], row['movie_name'], row['theater_name'], row['date'], row['time'], row['tickets'], row['total_price'])
        bookings.append(booking)

def show_movies():
    print("\nსეანსები:")
    for index, m in enumerate(movies):
        print(m.get_id()+ ".", m.get_title())
    print(f"{len(movies)+1}"+".", "გამოსვლა")

    try:
        user_choice = int(input("აირჩიეთ ფილმი ნომრით: "))
    except ValueError:
        print("გთხოვთ შეიყვანოთ რიცხვი!")
        return
    if user_choice == len(movies)+1:
        print("კარგად ბრძანდებოდეთ!")
        return
    chosen_movie = movies[user_choice - 1]
    show_movie_Details(chosen_movie)

def show_theaters_for_movie():
    for index, t in enumerate(theaters):
        print( t.get_id() + ".", t.get_name(), "-", t.get_location())

def show_movie_Details(chosen_movie):
    print(f"\nფილმის დასახელება: {chosen_movie.get_title()}")
    print(f"რეჟისორი: {chosen_movie.get_director()}")
    print(f"გამოშვების წელი: {chosen_movie.get_year()}")
    print(f"ხანგრძლივობა: {chosen_movie.get_duration()} წუთია\n")
    print("თეატრები სადაც ფილმი გადის:")
    show_theaters_for_movie()

    try:
        user_choice = int(input(f"აირჩიეთ კინოთეატრი ნომრით ან დაბრუნებისთვის {len(theaters)+1}-ს დააჭირეთ: "))
    except ValueError:
        print("გთხოვთ შეიყვანოთ რიცხვი!")
        return
    
    if user_choice == len(theaters)+1:
        show_movies()

    if 1 <= user_choice <= len(theaters):
        chosen_theater = theaters[user_choice - 1]
        print(f"\nთქვენ აირჩიეთ ფილმი '{chosen_movie.get_title()}' კინოთეატრში '{chosen_theater.get_name()}' მდებარეობით '{chosen_theater.get_location()}'")
        print("აირჩიეთ დღე:")
        for index, day in enumerate(days):
            print(f"{index + 1}. {day}")
        try:
            day_choice = int(input("აირჩიეთ დღე ნომრით: "))
        except ValueError:
            print("გთხოვთ შეიყვანოთ რიცხვი!")
            return
        print("აირჩიეთ დრო:")
        
        for index, t in enumerate(time):
            print(f"{index + 1}. {t}")
        try:
            time_choice = int(input("აირჩიეთ დრო ნომრით: "))
        except ValueError:
            print("გთხოვთ შეიყვანოთ რიცხვი!")
            return
        
        print("\nაირჩიეთ ადგილი:")
        seat_types = list(chosen_theater.get_seat_types())

        for index, seat in enumerate(seat_types):
            price = chosen_theater.get_seat_price(seat)
            print(f"{index + 1}. {seat} - {price} ლარი")

        seat_choice = int(input("აირჩიეთ ადგილი ნომრით: "))

        while seat_choice < 1 or seat_choice > len(seat_types):
            print("გთხოვთ აირჩიოთ  სწორი ადგილის ტიპი.")
            seat_choice = int(input("აირჩიეთ ადგილი ნომრით: "))

        seat_type = seat_types[seat_choice - 1]
        if bookings:
            booked_tickets = sum(int(b.get_tickets()) for b in bookings if b.get_theater_name() == chosen_theater.get_name() and b.get_date() == days[day_choice - 1] and b.get_time() == time[time_choice - 1])
        else:
            booked_tickets = 0

        available_tickets = chosen_theater.get_seat_capacity(seat_type) - booked_tickets
        if available_tickets == 0:
            print("ამ რიგში ადგილები აღარ არის ხელმისაწვდომი. გთხოვთ, აირჩიოთ სხვა ადგილი.")
            return

        seat_capacity = chosen_theater.get_seat_capacity(seat_type)
        number_of_tickets = int(input(f"რამდენი ბილეთი გინდათ? (მაქსიმუმ {seat_capacity}): "))
        #booking limit not meeting condition
        while(number_of_tickets > seat_capacity or number_of_tickets <= 0) :
            print(f"ბილეთების რაოდენობა არ უნდა აღემატებოდეს {available_tickets}.")
            if number_of_tickets == 0 :
                print("ბილეთების რაოდენობა უნდა იყოს მინიმუმ 1. გთხოვთ, სცადეთ თავიდან ცხოვრებაში. ")
            number_of_tickets = int(input(f"გთხოვთ, აირჩიოთ ვალიდური ბილეთების რაოდენობა (მაქსიმუმ {seat_capacity}): "))


        # number_of_tickets > 0 and number_of_tickets <= available_tickets:
        seat_price = chosen_theater.get_seat_price(seat_type)
        total_price = number_of_tickets * seat_price

        print(f"\nთქვენ აირჩიეთ {number_of_tickets} ბილეთი ფილმზე '{chosen_movie.get_title()}' კინოთეატრში '{chosen_theater.get_name()}' {days[day_choice - 1]}ს {time[time_choice - 1]} საათზე.")
        print(f"ბილეთების საერთო ღირებულებაა: {total_price} ლარი.")
        user_name = input("გთხოვთ შეიყვანოთ თქვენი სახელი: ")
        print(f"\nმადლობა {user_name}, თქვენი ჯავშანი მიღებულია!")
        with open("data/bookings.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([user_name, chosen_movie.get_title(), chosen_theater.get_name(), days[day_choice - 1], time[time_choice - 1], number_of_tickets, total_price])
        

print("1. დაჯავშნა")
print("2. სტატისტიკა")
user_input = input("აირჩიეთ ფუნქცია ნომრით: ")

if user_input == "2":
    print("\nსტატისტიკა - გაყიდული ბილეთების რაოდენობა ფილმების მიხედვით:")
else:
    

    
    
    show_movies()