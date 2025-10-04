
class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.status = False

    def start(self):
        if not self.status:
            self.status = True
            print(f'{self.name} is starting')
        else:
            print('is on dont start please')

    def off(self):
        if self.status:
            self.status = False
            print(f'{self.name} is of now')
        else:
            print('car is off please start frist')


car1 = Car("BMW", "123")

car1.start()
car1.start()

car1.off()
car1.off()
