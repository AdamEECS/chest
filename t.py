class A:
    def a(self, x):
        pass

    @classmethod
    def b(cls, x):
        pass

    @staticmethod
    def c(*args):
        pass

    def __getattribute__(self, item):
        if item in ['a', 'c']:
            return lambda *args: ', '.join([str(i) for i in args])


s = A()
print('a', s.c(1))
print('c', s.c(2, 'name'))
