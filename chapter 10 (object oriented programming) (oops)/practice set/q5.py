import random
class train():
    def __init__(self, user_name, destination, seat_price, total_seats = 100):
        self.user_name = user_name
        self.destination = destination
        self.seat_price = seat_price
        self.total_seats = total_seats
        self.booked_seats = 0

    def booking_a_ticket(self):
        user_destination = input("Enter the destination you want to go: ")
        if user_destination.lower() == self.destination.lower():
            self.booked_seats += 1 
            seat_number = random.randint(1, self.total_seats)
            print(f"Ticket booked successfully for {self.user_name}!")
            print(f"Destination: {self.destination}")
            print(f"Seat Number: {seat_number}")
            print(f"Fare: ₹{self.seat_price}")
        else:
            print("No seats available.")

train1 = train("Izumi", "Delhi", "3k")
train1.booking_a_ticket()

    
    

        
            

        

            

    
    

        

        
