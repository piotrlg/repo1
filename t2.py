__author__ = 'piotrlg'


class a_class(object):
    def __init__(self, a1):
        self.atr1 = a1
        pass

    def meth_1(self):
        pass

    def meth_2(self):
        pass


def main():
    a = a_class('jeden')
    b = a_class(33)

    print type(a.atr1), type(b.atr1)


if __name__ == '__main__':
    main()

