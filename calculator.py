import re


class Calculator(object):

    def add(self, x):
        if x == '':
            return 0
        else:
            if x.startswith('//'):
                delimiter = x[2]
                x = x.replace('//%s\n' % delimiter, '')
            else:
                delimiter = ','
            x = x.replace('\n', delimiter)
            x = x.replace(delimiter, ',')

            if len(x.split(',')) > 1:
                total = 0
                for num in x.split(','):
                    total += int(num)
                return total
            else:
                return int(x)
