from datetime import datetime


class Meeting:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


def check_availability(self, proposed_time):
    if self.end_time > proposed_time > self.start_time:
        return False
    else:
        return True

meetings = [Meeting(datetime(2018, 8, 1, 9, 0, 0), datetime(2018, 8, 1, 11, 0, 0)),
            Meeting(datetime(2018, 8, 1, 15, 0, 0), datetime(2018, 8, 1, 16, 0, 0)),
            Meeting(datetime(2018, 8, 2, 9, 0, 0), datetime(2018, 8, 2, 10, 0, 0))]
print(check_availability(meetings, datetime(2018, 8, 1, 12, 0, 0)))
print(check_availability(meetings, datetime(2018, 8, 1, 10, 0, 0)))