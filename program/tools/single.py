class Singleton(type):

    def __init__(cls, classname, superclases, attributes):
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            print('call')
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class T(metaclass=Singleton):
    def __init__(self):
        print('init')


test = T()
test = T()
test = T()
test = T()
test = T()
