class date:
    def accept(self):
        self.day = int(input('Enter Day : '))
        self.month = int(input('Enter Month : '))
        self.year = int(input('Enter Year : '))

    def display(self):
        print(f"{self.day}:{self.month}:{self.year}")

    def valid(self):
        if self.day >= 31:
            print('Invalid Date')
        elif self.month >= 12 :
            print(f"Invalid Date")


obj = date()

obj.accept()
obj.display()
obj.valid()