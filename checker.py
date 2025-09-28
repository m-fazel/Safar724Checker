import requests
import time
from playsound import playsound
from datetime import datetime
import json


# Function to check bus availability based on user-defined criteria
def check_buses(required_seats, date, destination, origin, price_limit, min_departure_time, max_departure_time,
                vip_required):
    url = f'https://service.safar724.com/buses/api/bus/route?Date={date}&Destination={destination}&Origin={origin}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        # Iterate over each bus in the response
        for bus in data.get("items", []):
            available_seats = bus["availableSeatCount"]

            # Apply user-defined filter criteria
            if available_seats >= required_seats and is_good_bus(bus, price_limit, min_departure_time,
                                                                 max_departure_time, vip_required):
                print(
                    f"Bus found! {available_seats} seats available on bus {bus['companyName']} at {bus['departureTime']}.")

                # Play a sound if a suitable bus is found
                playsound('./beep.mp3')
                return True

    except Exception as e:
        print(f"Error occurred: {e}")

    return False


# Define what makes a "good" bus based on user preferences
def is_good_bus(bus, price_limit, min_departure_time, max_departure_time, vip_required):
    price = bus['price']
    departure_time = bus['departureTime']
    is_vip = bus['isVip']

    # Check the bus against the user-defined criteria
    return (price <= price_limit and
            datetime.strptime(min_departure_time, "%H:%M").time() <= datetime.strptime(departure_time,
                                                                                       "%H:%M").time() <= datetime.strptime(
                max_departure_time, "%H:%M").time() and
            (not vip_required or is_vip))


# Main loop to keep checking
def monitor_buses(required_seats, date, destination, origin, price_limit, min_departure_time, max_departure_time,
                  vip_required):
    while True:
        check_buses(required_seats, date, destination, origin, price_limit, min_departure_time,
                    max_departure_time, vip_required)
        time.sleep(1)  # Wait for 60 seconds before checking again


# Get user input
date = input("Enter the date (in format YYYY-MM-DD, e.g., 1403-07-03): ")
origin = input("Enter the origin city (e.g., tehran): ")
destination = input("Enter the destination city (e.g., esfahan): ")
required_seats = int(input("Enter the number of seats you need: "))
price_limit = int(input("Enter the maximum price you're willing to pay (e.g., 2600000): "))
min_departure_time = input("Enter the earliest departure time (in format HH:MM, e.g., 06:00): ")
max_departure_time = input("Enter the latest departure time (in format HH:MM, e.g., 18:00): ")
vip_required = input("Do you want only VIP buses? (yes/no): ").strip().lower() == 'yes'

# Start monitoring buses
monitor_buses(required_seats, date, destination, origin, price_limit, min_departure_time, max_departure_time,
              vip_required)
