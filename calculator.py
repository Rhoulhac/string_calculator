class Calculator(object):

    def add(self, x):
        if len(x.split(',')) == 2:
            return int(x.split(',')[0]) + int(x.split(',')[1])
        elif x == '':
            return 0
        else:
            return int(x)
