class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

if __name__ == "__main__":
    person = Person("John", "Smith")
    print(person.firstName)
    print(person.lastName)