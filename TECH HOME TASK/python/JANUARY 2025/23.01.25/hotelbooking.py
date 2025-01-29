class HotelRoom:
    def __init__(self):
        self.__room_number = None
        self.__is_occupied = False
        self.__rate_per_night = None

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        if isinstance(room_number, int) and room_number > 0:
            self.__room_number = room_number
        else:
            raise ValueError("Room number must be a positive integer.")

    def get_rate_per_night(self):
        return self.__rate_per_night

    def set_rate_per_night(self, rate_per_night):
        if isinstance(rate_per_night, (int, float)) and rate_per_night > 0:
            self.__rate_per_night = rate_per_night
        else:
            raise ValueError("Rate per night must be a positive number.")

    def check_in(self):
        if self.__is_occupied:
            raise Exception("Room is already occupied.")
        self.__is_occupied = True

    def check_out(self):
        if not self.__is_occupied:
            raise Exception("Room is already vacant.")
        self.__is_occupied = False

    def display_details(self):
        occupied_status = "Yes" if self.__is_occupied else "No"
        print(f"Room Number: {self.__room_number}")
        print(f"Rate per Night: ${self.__rate_per_night:.2f}")
        print(f"Occupied: {occupied_status}")
room = HotelRoom()
room.set_room_number(101)
room.set_rate_per_night(200.50)
room.display_details()

