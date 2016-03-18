UP = 1
DOWN = 2
FLOOR_COUNT = 6

class ElevatorLogic(object):
    """
    An incorrect implementation. Can you make it pass all the tests?

    Fix the methods below to implement the correct logic for elevators.
    The tests are integrated into `README.md`. To run the tests:
    $ python -m doctest -v README.md

    To learn when each method is called, read its docstring.
    To interact with the world, you can get the current floor from the
    `current_floor` property of the `callbacks` object, and you can move the
    elevator by setting the `motor_direction` property. See below for how this is done.
    """

    def __init__(self):
        # Feel free to add any instance variables you want.
        self.destination_floor = None
        self.floorStack = []
        self.directionStack = []
        self.lastDirection = None
        self.callbacks = None

    def on_called(self, floor, direction):
        """
        This is called when somebody presses the up or down button to call the elevator.
        This could happen at any time, whether or not the elevator is moving.
        The elevator could be requested at any floor at any time, going in either direction.

        floor: the floor that the elevator is being called to
        direction: the direction the caller wants to go, up or down
        """
        self.destination_floor = floor
        self.floorStack.append(floor)
        self.lastDirection = direction
        self.directionStack.append(direction)

    def on_floor_selected(self, floor):
        """
        This is called when somebody on the elevator chooses a floor.
        This could happen at any time, whether or not the elevator is moving.
        Any floor could be requested at any time.

        floor: the floor that was requested
        """
        if self.callbacks.motor_direction == UP:
            if floor > self.callbacks.current_floor:
                self.destination_floor = floor
                self.floorStack.append(floor)
        if self.callbacks.motor_direction == DOWN:
            if floor < self.callbacks.current_floor:
                self.destination_floor = floor
                self.floorStack.append(floor)
        if self.callbacks.motor_direction == None:
            self.destination_floor = floor
            self.floorStack.append(floor)

    def on_floor_changed(self):
        """
        This lets you know that the elevator has moved one floor up or down.
        You should decide whether or not you want to stop the elevator.
        """

        # if self.floorStack:
        if self.lastDirection == self.callbacks.motor_direction:
            if self.floorStack[0] == self.callbacks.current_floor:
                self.callbacks.motor_direction = None
                del self.floorStack[0]
        # elif self.lastDirection != self.callbacks.motor_direction:
        #     if self.floorStack[0] == self.callbacks.current_floor:
        #         self.callbacks.motor_direction = None
        #         del self.floorStack[0]
            # elif self.floorStack[-1] != self.callbacks.current_floor:
                # self.callbacks.motor_direction = self.directionStack.pop()

    def greaterThanCurrentFloor(x):
        return x > self.callbacks.current_floor

    def lessThanCurrentFloor(x):
        return x < self.callbacks.current_floor

    def on_ready(self):
        """
        This is called when the elevator is ready to go.
        Maybe passengers have embarked and disembarked. The doors are closed,
        time to actually move, if necessary.
        """
        # if self.floorStack:
        #     if self.callbacks.motor_direction == UP:
        #         workingStack = filter(self.floorStack > self.callbacks.current_floor)
        #         workingStack.sort()
        #         if self.workingStack[-1] == self.callbacks.current_floor:
        #             self.callbacks.motor_direction = None
        #             self.floorStack.pop()
        #     if self.callbacks.motor_direction == DOWN:
        #         workingStack = filter(self.floorStack < self.callbacks.current_floor)
        #         workingStack.sort()
        #         if self.workingStack[-1] == self.callbacks.current_floor:
        #             self.callbacks.motor_direction = None
        #             self.floorStack.pop()
        #     if self.callbacks.motor_direction == None:
        # if self.floorStack[-1] != self.callbacks.current_floor:
            # self.callbacks.motor_direction = self.directionStack[-1]

        # if self.floorStack:
        #     if self.floorStack[-1] > self.callbacks.current_floor:
        #         workingStack = filter(greaterThanCurrentFloor, self.floorStack)
        #         workingStack.sort(reverse=True)
        #         self.callbacks.motor_direction = UP
        #     if self.floorStack[-1] < self.callbacks.current_floor:
        #         workingStack = filter(lessThanCurrentFloor, self.floorStack)
        #         workingStack.sort(reverse=True)
        #         self.callbacks.motor_direction = DOWN

        if self.floorStack[0] > self.callbacks.current_floor:
            self.callbacks.motor_direction = UP
            self.lastDirection = UP
        elif self.floorStack[0] < self.callbacks.current_floor:
            self.callbacks.motor_direction = DOWN
            self.lastDirection = DOWN
