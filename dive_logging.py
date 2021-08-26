
class Dive:
    def __init__(self, pressure_start, pressure_finish, time_start, time_finish, depth):
        self.pressure_start = pressure_start
        self.pressure_finish = pressure_finish
        self.time_start = time_start
        self.time_finish = time_finish
        self.depth = depth

    def get_SACR(self):
        return (33 * (self.pressure_start - self.pressure_finish))/(self.time(self.depth + 33))

    @staticmethod
    def time_processing(time_format):
        time_list = list(map(int, time_format.split(':')))
        return (60*time_list[0]) + time_list[1]

    def get_duration(self):
        return self.time_processing(self.time_finish) - self.time_processing(self.time_start)

    def __str__(self):
        return "Dive(start={}, finish={}, in={}, out={}, depth={})".format(
            self.pressure_start, self.pressure_finish, self.time_start, self.time_finish, self.depth
        )
