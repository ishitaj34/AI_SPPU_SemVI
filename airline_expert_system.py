from colorama import init, Fore, Style
init(autoreset=True)

class Flight:
    def __init__(self, flight_id, aircraft_id, origin, destination, departure_time, arrival_time, cargo_weight, is_emergency, weather_score):
        self.flight_id = flight_id
        self.aircraft_id = aircraft_id
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.cargo_weight = cargo_weight
        self.is_emergency = is_emergency
        self.weather_score = weather_score
        self.status = "Scheduled"

class ExpertSystem:
    def __init__(self):
        self.flights = []
        self.aircraft_schedule = {}  
        self.restricted_hours = {"Delhi": [(2, 4)]}

    def add_flight(self, flight):
        print(f"\n{Fore.BLUE}{Style.BRIGHT}--- Evaluating flight {flight.flight_id} ---{Style.RESET_ALL}")
        if self.weather_check(flight):
            if self.no_fly_zone_check(flight):
                if self.check_aircraft_availability(flight):
                    if self.check_time_conflict(flight):
                        if self.check_cargo_limit(flight):
                            self.flights.append(flight)
                            self.schedule_aircraft(flight)
                            print(f"{Fore.GREEN}✅ Flight scheduled successfully.")
                        else:
                            print(f"{Fore.RED}❌ Cargo exceeds limit (Max 5000kg). Flight rejected.")
                    else:
                        print(f"{Fore.RED}❌ Time slot conflict detected. Flight rejected.")
                else:
                    print(f"{Fore.RED}❌ Aircraft already assigned to another flight at this time.")
            else:
                print(f"{Fore.RED}❌ Flight scheduled during restricted hours.")
        else:
            print(f"{Fore.RED}❌ Weather risk too high. Flight delayed.")

    
    def check_time_conflict(self, new_flight):
        for flight in self.flights:
            if flight.origin == new_flight.origin and flight.destination == new_flight.destination:
                if not (new_flight.arrival_time <= flight.departure_time or new_flight.departure_time >= flight.arrival_time):
                    if not new_flight.is_emergency:
                        return False
        return True

    def check_aircraft_availability(self, flight):
        schedule = self.aircraft_schedule.get(flight.aircraft_id, [])
        for (start, end) in schedule:
            if not (flight.arrival_time <= start or flight.departure_time >= end):
                return False
        return True

    def schedule_aircraft(self, flight):
        if flight.aircraft_id not in self.aircraft_schedule:
            self.aircraft_schedule[flight.aircraft_id] = []
        self.aircraft_schedule[flight.aircraft_id].append((flight.departure_time, flight.arrival_time))

    def check_cargo_limit(self, flight):
        return flight.cargo_weight <= 5000

     def no_fly_zone_check(self, flight):
        if flight.origin in self.restricted_hours:
            for (start, end) in self.restricted_hours[flight.origin]:
                if start <= flight.departure_time < end:
                    if not flight.is_emergency:
                        return False
        return True

    def weather_check(self, flight):
        if flight.weather_score > 6 and not flight.is_emergency:
            flight.status = "Delayed due to weather"
            return False
        return True

    def display_flights(self):
        if not self.flights:
            print(f"{Fore.YELLOW}⚠️  No flights scheduled.")
        for f in self.flights:
            print(f"\n{Fore.MAGENTA}Flight ID: {f.flight_id}")
            print(f"{Fore.CYAN}Aircraft: {f.aircraft_id}")
            print(f"{Fore.YELLOW}From: {f.origin} → To: {f.destination}")
            print(f"{Fore.BLUE}Time: {f.departure_time} to {f.arrival_time}")
            print(f"{Fore.GREEN}Cargo Weight: {f.cargo_weight}kg")
            print(f"{Fore.MAGENTA}Emergency: {'Yes' if f.is_emergency else 'No'}")
            print(f"{Fore.YELLOW}Weather Risk: {f.weather_score}")
            print(f"{Fore.CYAN}Status: {f.status}")

def get_flight_input():
    print(f"\n{Fore.BLUE}--- Enter Flight Details ---")
    flight_id = input("Enter Flight ID: ")
    aircraft_id = input("Enter Aircraft ID: ")
    origin = input("Enter Origin City: ")
    destination = input("Enter Destination City: ")
    departure_time = int(input("Enter Departure Time (0–24): "))
    arrival_time = int(input("Enter Arrival Time (0–24): "))
    cargo_weight = int(input("Enter Cargo Weight (kg): "))
    is_emergency = input("Is it an emergency flight? (yes/no): ").strip().lower() == "yes"
    weather_score = int(input("Enter Weather Risk Score (0–10): "))
    return Flight(flight_id, aircraft_id, origin, destination, departure_time, arrival_time, cargo_weight, is_emergency, weather_score)

def menu():
    system = ExpertSystem()
    while True:
        print(f"\n{Fore.LIGHTBLUE_EX}========== AIRLINE & CARGO SCHEDULER ==========")
        print("1. Add a New Flight")
        print("2. View Scheduled Flights")
        print("3. Exit")
        choice = input(f"{Fore.YELLOW}Enter your choice: {Style.RESET_ALL}")

        if choice == "1":
            flight = get_flight_input()
            system.add_flight(flight)
        elif choice == "2":
            print(f"\n{Fore.LIGHTMAGENTA_EX}--- Scheduled Flights ---")
            system.display_flights()
        elif choice == "3":
            print(f"{Fore.GREEN}Exiting... ✈️")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Try again.")

if __name__ == "__main__":
    menu()

