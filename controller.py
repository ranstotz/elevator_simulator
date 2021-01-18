import queue
import threading
import time


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper


class Elevator_controller():
    def __init__(self):
        print('starting... \n')
        num_floors = 10
        self.fifo_queue = queue.Queue()
        self.floors = [i for i in range(num_floors)]
        self.up_targets = [False for i in range(num_floors)]
        self.down_targets = [False for i in range(num_floors)]
        self.current_floor = 0  # start at the bottom floor -- in our case 0
        self.is_on = True

    def get_outside_input(self, pickup_floor, direction):
        # this is when the user is calling the elevator to come to them
        # if up, add to up targets
        # ignore input where a user hits up then selects a floor below them and vice versa
        if direction == 'UP':
            # add to
            self.up_targets[pickup_floor]
        if direction == 'DOWN':
            self.up_targets[pickup_floor]

        return

    def get_inside_input(self, target_floor):
        # part of the algo relies on the assumption (for now) that only people going up
        # or down will be in the car at a time (ideally)
        if target_floor > self.current_floor:
            self.up_targets[target_floor] == True
        if target_floor < self.current_floor:
            self.down_targets[target_floor] == True
        return

    def travel_up(self):
        # first get targets
        return

    def make_stop(self, floor):
        # simulate opening elevator door
        # have some side effect
        print("Making stop at floor: ", floor)
        self.fifo_queue.put(floor)

    @threaded
    def run(self):
        print("running")
        while True:
            while not self.fifo_queue.empty():
                print("run thread queue get: ", self.fifo_queue.get())
            # let the thread sleep for a tick to not kill the fan
            time.sleep(0.5)

        return

    def get_current_floor(self):
        return self.current_floor

    def set_current_floor(self, floor):
        self.current_floor = floor
        print("elevator at floor: ", self.current_floor)
        return


if __name__ == "__main__":
    elevator = Elevator_controller()
    thread = elevator.run()

    elevator.make_stop(1)
    elevator.make_stop(5)
    while True:
        num = input("Enter number :")
        elevator.make_stop(num)
        time.sleep(0.1)  # let the thread sleep for a tick to not kill the fan
    thread.join()
