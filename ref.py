from typing import List, Dict
from dataclasses import dataclass
from enum import Enum


@dataclass
class Test:
    id: int = None
    name: str = None


def sort_test(lst):
    return sorted(lst, key=lambda a: a.id)


class FibonacciSequence:
    n: int = None
    start: int = None

    def __init__(self, n: int = 1, start: int = 1):
        assert n > 0 and start > 0, 'Both n and start need to be greater than 0'
        self.start_n = start-1  # -- this makes the sequence inclusive of start n-th element
        self.n = n

    def __next__(self):
        # cached fib(n-1) and fib(n-2)
        fib_n_minus_1 = 1
        fib_n_minus_2 = 1
        for n in range(self.n):
            if n < 2:
                fib_n = 1
            else:
                fib_n = fib_n_minus_1 + fib_n_minus_2
            if n >= self.start_n:
                yield fib_n
            fib_n_minus_2 = fib_n_minus_1
            fib_n_minus_1 = fib_n


class Bracket(Enum):
    CURLY = ('{', '}')
    ROUND = ('(', ')')
    SQUARE = ('[', ']')

    def __init__(self, open_bracket, close_bracket):
        self.open_bracket = open_bracket
        self.close_bracket = close_bracket


class BracketCheck(object):
    brackets_by_open: Dict[str, Bracket] = None  # -- need this to check for open bracket
    brackets_by_close: Dict[str, Bracket] = None  # -- need this to check for close bracket

    def __init__(self):

        self.brackets_by_open = {brack.open_bracket: brack for brack in Bracket}
        self.brackets_by_close = {brack.close_bracket: brack for brack in Bracket}

    def is_open_bracket(self, letter: str) -> bool:
        return letter in self.brackets_by_open

    def is_close_bracket(self, letter: str) -> bool:
        return letter in self.brackets_by_close

    def is_bracket(self, letter: str) -> bool:
        return self.is_open_bracket(letter) or self.is_close_bracket(letter)

    def check_line(self, line):
        # -- need a stack to keep track of brackets encountered
        stack: List[str] = list()

        for letter in line:
            if not self.is_bracket(letter):
                continue

            if self.is_open_bracket(letter):
                stack.append(letter)
                print(stack)
                continue

            # -- the letter is a close bracket here
            # -- first check whether the stack is empty
            if not bool(stack):
                print('there is no open bracket for  %s' % letter)
                return 0  # -- there's a close bracket without a open bracket

            # -- peek the top of the stack to see if we have a matching open bracket
            if self.brackets_by_close[letter].open_bracket == stack[-1]:
                # -- bracket is closed
                stack.pop()
                print(stack)
            else:
                # -- we have a close bracket without a matching open bracket
                print('there is no open bracket for %s' % letter)
                return 0

        # -- we are out of the for loop so all letters for the line were checked
        # -- if the stack is not empty then we have unmatched open brackets
        if bool(stack):
            print('not closed %s' % stack)
            return 0
        else:
            return 1


# -- need an enumeration for spot type
class SpotType(Enum):
    MOTOR_CYCLE = 1
    CAR = 2
    REGULAR = 3


class VehicleType(Enum):
    MOTOR_CYCLE = ((SpotType.MOTOR_CYCLE, SpotType.CAR, SpotType.REGULAR), 1)
    CAR = ((SpotType.CAR, SpotType.REGULAR), 1)
    VAN = ((SpotType.REGULAR,), 3)

    def __init__(self, spots_allowed, spots_required):
        self.spots_allowed = spots_allowed
        self.spots_required = spots_required


# -- need a class for vehicle
@dataclass
class Vehicle:
    v_id: int = None
    v_type: VehicleType = None
    spot_used: SpotType = None


@dataclass
class SpotsAllowed:
    spot_types: List[SpotType] = None
    spots_required: int = None


class ParkingLot:
    def __init__(self, spots: Dict[SpotType,int]):
        self.all_spots = spots
        self.spots = {k: 0 for k, v in self.all_spots.items()}  # -- keep track spot taken

    def find_open_spot(self, v_type: VehicleType) -> SpotType:
        for spot_type in v_type.spots_allowed:
            if self.open_spots(spot_type) >= v_type.spots_required:
                return spot_type

    def park(self, vehicle: Vehicle):
        found_open_spot = self.find_open_spot(vehicle.v_type)
        if bool(found_open_spot):
            self.spots[found_open_spot] += vehicle.v_type.spots_required
            vehicle.spot_used = found_open_spot

    def leave(self, vehicle: Vehicle):
        if bool(vehicle.spot_used):
            self.spots[vehicle.spot_used] -= vehicle.v_type.spots_required
            vehicle.spot_used = None

    def total_spots(self) -> int:
        return sum((v for v in self.all_spots.values()))

    def open_spots(self, spot_type: SpotType = None) -> int:
        if not bool(spot_type):
            return sum((self.all_spots[k]-v for k, v in self.spots.items()))
        else:
            return self.all_spots[spot_type] - self.spots[spot_type]

    def is_full(self) -> bool:
        return self.open_spots() == 0

    def is_empty(self) -> bool:
        return self.open_spots() == self.total_spots()

    def spots_taken(self) -> int:
        return sum((v for v in self.spots.values()))


def main():
    vehicles = [
        Vehicle(1, VehicleType.CAR),Vehicle(2, VehicleType.VAN),Vehicle(1, VehicleType.VAN),
        Vehicle(1, VehicleType.CAR),Vehicle(1, VehicleType.CAR),Vehicle(1, VehicleType.CAR),
        Vehicle(1, VehicleType.CAR),Vehicle(1, VehicleType.CAR),Vehicle(1, VehicleType.CAR),
        Vehicle(1, VehicleType.MOTOR_CYCLE),Vehicle(1, VehicleType.MOTOR_CYCLE),Vehicle(1, VehicleType.CAR),
        Vehicle(1, VehicleType.MOTOR_CYCLE),Vehicle(1, VehicleType.MOTOR_CYCLE),Vehicle(1, VehicleType.CAR),
        Vehicle(1, VehicleType.MOTOR_CYCLE),Vehicle(1, VehicleType.MOTOR_CYCLE),Vehicle(1, VehicleType.CAR),
        Vehicle(1, VehicleType.MOTOR_CYCLE),Vehicle(1, VehicleType.MOTOR_CYCLE),Vehicle(1, VehicleType.CAR),
    ]

    lot_22 = ParkingLot(
        spots={
            SpotType.MOTOR_CYCLE: 5,
            SpotType.CAR: 8,
            SpotType.REGULAR: 5,
        }
    )

    for vehicle in vehicles:
        lot_22.park(vehicle)
        if bool(vehicle.spot_used):
            print('Parked %s in %s, taken=%d, open=%d' % (
                vehicle.v_type, vehicle.spot_used, lot_22.spots_taken(), lot_22.open_spots())
            )
        elif lot_22.is_full():
            print('Sorry lot full')
        else:
            print('Sorry no room for your vehicle type %s ' % vehicle.v_type)

    for vehicle in vehicles:
        if vehicle.spot_used:
            spot_used = vehicle.spot_used
            lot_22.leave(vehicle)
            print('%s leaving %s, taken=%d, open=%d' % (
                vehicle.v_type, spot_used, lot_22.spots_taken(), lot_22.open_spots())
            )


# /*
# Design a parking lot using object-oriented principles
#
# Goals:
# - Your solution should be in Java - if you would like to use another language, please let the interviewer know.
# - Boilerplate is provided. Feel free to change the code as you see fit
#
# Assumptions:
# - The parking lot can hold motorcycles, cars and vans
# - The parking lot has motorcycle spots, car spots and large spots
# - A motorcycle can park in any spot
# - A car can park in a single compact spot, or a regular spot
# - A van can park, but it will take up 3 regular spots
# - These are just a few assumptions. Feel free to ask your interviewer about more assumptions as needed
#
# Here are a few methods that you should be able to run:
# - Tell us how many spots are remaining
# - Tell us how many total spots are in the parking lot
# - Tell us when the parking lot is full
# - Tell us when the parking lot is empty
# - Tell us when certain spots are full e.g. when all motorcycle spots are taken
# - Tell us how many spots vans are taking up
#
# Hey candidate! Welcome to your interview. I'll start off by giving you a Solution class.
# To run the code at any time, please hit the run button located in the top left corner.


def main1():
    # test_list: List[Test] = [Test(id=11, name='one'), Test(id=2, name='two'), Test(id=13, name='three')]
    # print('Test')
    # print(sort_test(test_list))
    # print(VehicleType.MOTOR_CYCLE)
    # print(VehicleType.MOTOR_CYCLE.spots_allowed)

    # check_brackets = BracketCheck()
    # print(check_brackets.check_line('((djhkkf)fjhfkjk)[dfhh]{fdf}'))
    # print(check_brackets.check_line('((djhkkffjhfkjk)[dfhh]{fdf}'))
    # print(check_brackets.check_line('((djhkkf)fjhfkjk)[dfhh]fdf}'))
    # print(check_brackets.check_line('((djhkkf)fjhfkjk)dfhh]{fdf}'))

    print([i for i in next(FibonacciSequence(20))])


if __name__ == "__main__":
    main()

