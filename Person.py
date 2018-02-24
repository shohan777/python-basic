class Person:
    name = ''
    location = ''

    def detail(self, name, location):
        self.name = name
        self.location = location
        print('You {a} and live in {b}', format(self.name, self.location))


person = Person
person.detail('Shohan', 'Dhaka')
