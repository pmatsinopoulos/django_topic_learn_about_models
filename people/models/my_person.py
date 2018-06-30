from .person import Person


class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        print("I am doing something different as a {}".format(self.__class__))
