class Person:
    name = ''
    location = ''

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def detail(self):
        print('You {a} and live in {b}'.format(a=self.name, b=self.location))


person = Person('Shohan', 'Dhaka')
person.detail()
