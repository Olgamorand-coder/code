from datetime import datetime


class Meeting:
    def __init__(self, start_time, end_time, room):
        self.start_time = start_time
        self.end_time = end_time
        self.room = room

    # checks if proposed time is in meeting time
    def check_in_meeting_time(self, proposed_time):
        return self.start_time < proposed_time < self.end_time

    def is_overlapping(self, another_meeting):
        return (self.check_in_meeting_time(another_meeting.start_time) or
                self.check_in_meeting_time(another_meeting.end_time)) and \
               (self.room == another_meeting.room)


class Employee:
    def __init__(self):
        self.meetings = []

    def add_meeting(self, meeting):
        if self.check_availability(meeting.start_time) and self.check_availability(meeting.end_time):
            self.meetings.append(meeting)
        else:
            return False

    def check_availability(self, proposed_time):
        for meeting in self.meetings:
            if meeting.check_in_meeting_time(proposed_time):
                return False
        return True


empl1 = Employee()
empl1.add_meeting(Meeting(datetime(2018, 8, 1, 9, 0, 0), datetime(2018, 8, 1, 11, 0, 0)))

meetings = [,
            Meeting(datetime(2018, 8, 1, 15, 0, 0), datetime(2018, 8, 1, 16, 0, 0)),
            Meeting(datetime(2018, 8, 2, 9, 0, 0), datetime(2018, 8, 2, 10, 0, 0))]
print(check_availability(meetings, datetime(2018, 8, 1, 12, 0, 0)))
print(check_availability(meetings, datetime(2018, 8, 1, 10, 0, 0)))

meeting1= Meeting(datetime(2018, 8, 1, 9, 0, 0), datetime(2018, 8, 1, 11, 0, 0))
meeting2 = Meeting(datetime(2018, 8, 1, 15, 0, 0), datetime(2018, 8, 1, 16, 0, 0))

print(meeting1.is_overlapping(meeting2))