
from collections import defaultdict


class Sample:
    def __init__(self, *args):
        self.args = [*args]

    def __str__(self):
        pass

    def mean(self):
        try:
            return sum(self.args) / len(self.args)
        except ZeroDivisionError:
            return

    @staticmethod
    def find_frequency(args):
        frequency = {}
        for arg in args:
            if arg not in frequency:
                frequency[arg] = 1
            else:
                frequency[arg] += 1
        return frequency

    def mode(self):
        frequency = Sample.find_frequency(self.args)
        by_frequency = defaultdict(list)
        for key in frequency:
            by_frequency[frequency[key]].append(key)
        if by_frequency:
            return by_frequency[max(by_frequency)]

    def median(self):
        length = len(self.args)
        arg_sample = sorted(self.args)

        if length % 2 == 1:
            return arg_sample[length // 2]
        else:
            return (arg_sample[length // 2] + arg_sample[(length // 2) - 1]) / 2

    def variance(self):
        if len(self.args) < 2:
            return
        return sum(map(lambda x: (x-self.mean())**2, self.args))/(len(self.args)-1)

    def stdev(self):
        return self.variance() ** 2
