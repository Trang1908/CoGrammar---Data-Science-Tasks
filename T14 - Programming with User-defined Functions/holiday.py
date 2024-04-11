# Require user to enter the input

# The city they will be flying to
print("The cities include: \n London \n Paris \n Berlin")
city_flight = input("Please enter the city you will fly to: ")

# The number of nights they will be staying at the hotel and number of days for hiring car
while True:
    try:
        num_nights = int(input("Please enter the number of nights you will be staying at a hotel: "))
        rental_days = int(input("Please enter the number of days for which you will be hiring a car: "))
        break
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
    continue

# Create a function for the cost of the flight
def plane_cost(city):
    cities_list = {"London": 10,
              "Paris": 20,
              "Berlin": 30}
    return cities_list[city_flight]

print(f"The cost of your flight to {city_flight} is: £{plane_cost(city_flight)}")

# Create a function for a total cost of the hotel stay
def hotel_cost(number_of_night):
    price = number_of_night * 11.2
    return price

print(f"The toal cost for staying at hotel during {num_nights} nights is: £{hotel_cost(num_nights)}")

# Create a function for the total cost of car rental
def car_rental(days):
    price = rental_days*2.1
    return price

print(f"The cost for hiring car in {rental_days} days is: £{car_rental(rental_days)}")

# Create a function for the total cost of the holiday
def holiday_cost(hotel, flight, car):
    hotel_staying = hotel_cost(hotel)
    flight_price = plane_cost(flight)
    car_hiring = car_rental(car)
    return(hotel_staying + flight_price + car_hiring)

print(f"The total cost of your holiday is: £{holiday_cost(num_nights, city_flight, rental_days)}")