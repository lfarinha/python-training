from datetime import date


class Person:
    first_name = None
    last_name = None

    # CONSTRUCTOR
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # setter and getter

    def caculate_age(self, year_of_birth):
        return 2020 - int(year_of_birth)

    def set_name(self, name):
        self.first_name = name

    def get_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name


if __name__ == '__main__':
    personas = list()
    personas.append(Person("Daniel", "De Crescenzo"))
    personas.append(Person("Leonardo", "Farinha"))

    for person in personas:
        print(person.get_name(), person.get_last_name())
