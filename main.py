import random
from linkedlist import LinkedList

if __name__ == '__main__':
    # store months of the year.
    # uses a list to access at index
    months_in_year = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                      'november', 'december']

    pi_day = months_in_year[2]
    print(f"The month of pi is in {pi_day}\n")

    # store locations where you have celebrated your birthday
    # uses a set to add and iterate over values
    bday_locations = {'virginia, us', 'north carolina, us', 'california, us', 'drc, africa', 'germany, europe'}
    bday_locations.add('ghana, africa')
    bday_locations.add('nevada, us')
    bday_locations.add('georgia, us')
    # iterate over the set of values
    for location in bday_locations:
        print(location)

    # store sweep_stakes contestants.
    class Sweepstakes:
        def __init__(self):
            self.contestants = {}
            self.key = 1

        def add_contestant(self, first_name, last_name):
            self.contestants[self.key] = f"{first_name} {last_name}"
            self.key += 1

        def select_winner(self):
            rand = random.randrange(1, 6)
            winner = self.contestants[rand]
            print(f"\nAnd the winner is... {winner}!")

    sweepstakes = Sweepstakes()
    sweepstakes.add_contestant('bruce', 'lee')
    sweepstakes.add_contestant('jackie', 'chan')
    sweepstakes.add_contestant('jet', 'li')
    sweepstakes.add_contestant('michael jai', 'white')
    sweepstakes.add_contestant('chuck', 'norris')
    print(f"\n{sweepstakes.contestants}")
    sweepstakes.select_winner()

    # use list to store immediate family
    immediate_family = [{"first name": "charles",
                         "last name": "nesmith",
                         "relation": "father"},
                        {"first name": "gloria",
                         "last name": "nesmith",
                         "relation": "mother"},
                        {"first name": "kamilah",
                         "last name": "nesmith",
                         "relation": "sister"},
                        {"first name": "maurice",
                         "last name": "thomas",
                         "relation": "nephew"}]
    print(f"\n{immediate_family}")

    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
