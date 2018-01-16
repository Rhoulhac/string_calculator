class Calculator(object):

    def add(self, x):
        if len(x.split(',')) > 1:
            total = 0
            for num in x.split(','):
                total += int(num)
            return total
        elif x == '':
            return 0
        else:
            return int(x)
