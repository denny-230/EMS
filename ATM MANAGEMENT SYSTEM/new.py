# Constants
NUM_FLOORS = 10
MAX_CAPACITY = 20

# Elevator variables
current_floor = 0
current_capacity = 0

# Semaphore and condition variables
elevator_mutex = Semaphore(1)  # To ensure mutual exclusion for elevator variables
user_condition = Condition()  # To signal when the elevator has reached the desired floor

# Elevator thread function
def elevator_thread():
    while True:
        # Move the elevator to the next floor
        move_elevator()

        # Notify waiting users if the elevator has reached their desired floor
        with elevator_mutex:
            user_condition.notify_all()

# User thread function
def user_thread(from_floor, to_floor):
    with elevator_mutex:
        # Wait until the elevator is at the user's current floor
        while current_floor != from_floor:
            user_condition.wait()

        # Enter the elevator
        current_capacity += 1

        # Wait until the elevator reaches the user's desired floor
        while current_floor != to_floor:
            user_condition.wait()

        # Exit the elevator
        current_capacity -= 1

        # Signal that the elevator has reached the user's desired floor
        user_condition.notify_all()

# Helper function to move the elevator
def move_elevator():
    # Move the elevator up or down based on the current and desired