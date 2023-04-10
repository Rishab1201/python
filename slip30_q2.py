class Country:
    def __init__(self):
        self.nationality = ""

    def printNationality(self):
        print("Nationality:", self.nationality)

class State(Country):
    def __init__(self):
        super().__init__()
        self.stateName = ""

    def printState(self):
        print("State:", self.stateName)

    def printDetails(self):
        print("State:", self.stateName)
        super().printNationality()

# create an object of State class
state = State()

# accept state name and nationality from user
state.stateName = input("Enter state name: ")
state.nationality = input("Enter nationality: ")

# print state, country and nationality
state.printDetails()
