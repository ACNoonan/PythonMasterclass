class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, I'm flying!")
        elif self.ratio == 1:
            print("I'm hanging in here mann")
        else:
            print('That is not funny.')


class Duck:

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print('waddling')

    def swim(self):
        print('swimming')

    def quack(self):
        print('quacking')

    def fly(self):
        self._wing.fly()


class Penguin:

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print('waddling2')

    def swim(self):
        print('swimming2')

    def quack(self):
        print('quacking2')

    def aviate(self):
        print('I won the lottery and bought a learjet')


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


class Mallard(Duck):
    pass


class Flock:

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, 'fly', None)
        # if type(duck) is Duck:
        # if isinstance(duck, Duck):
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception handling in migrate")  # TODO remove this before release
            except AttributeError as e:
                print('One duck down')
                problem = e
            if problem:
                raise problem

if __name__ == '__main__':
    donald = Duck()
    donald.fly()

