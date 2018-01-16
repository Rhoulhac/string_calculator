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
                negatives = []
                for num in x.split(','):
                    if num.startswith('-'):
                        negatives += [num]
                    else:
                        total += int(num)
                if negatives:
                    raise Exception('negatives not allowed: ' + ','.join(negatives))
                else:
                    return total
            else:
                return int(x)
