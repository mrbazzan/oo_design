
class Dive:
    def __init__(self, pressure_start, pressure_finish, time_start, time_finish, depth):
        self.pressure_start = pressure_start
        self.pressure_finish = pressure_finish
        self.time_start = time_start
        self.time_finish = time_finish
        self.depth = depth

    def get_SACR(self):
        return (33 * (self.pressure_start - self.pressure_finish)) / (self.get_duration() * (self.depth + 33))

    @staticmethod
    def time_processing(time_format):
        time_list = list(map(int, time_format.split(':')))
        return (60 * time_list[0]) + time_list[1]

    def get_duration(self):
        return self.time_processing(self.time_finish) - self.time_processing(self.time_start)

    def __str__(self):
        return "Dive(start={}, finish={}, in='{}', out='{}', depth={})".format(
            self.pressure_start, self.pressure_finish, self.time_start, self.time_finish, self.depth
        )


class DiveLog:
    def __init__(self, *listOfDives):
        self.dives = listOfDives
        self.length = len(self.dives)

    def get_avg_SACR(self):
        return sum(dive.get_SACR() for dive in self.dives)/self.length


log = DiveLog(
    Dive(3100, 1300, "11:52", "12:45", 35),
    Dive(2700, 1000, "11:16", "12:06", 40),
    Dive(2800, 1200, "11:26", "12:06", 60),
    Dive(2800, 1150, "11:54", "12:16", 95),
)

print('Average SACR: ', log.get_avg_SACR())
print('\n', end='')
for dive in log.dives:
    print(dive)
