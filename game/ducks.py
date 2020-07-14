class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print('I am now flying')
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

    def walk(self):
        print('waddling2')

    def swim(self):
        print('swimming2')

    def quack(self):
        print('quacking2')


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':
    donald = Duck()
    donald.fly()

