from datetime import datetime

class Attendance:
    def __init__(self):
        self.check_in_time = None
        self.check_out_time = None

    def check_in(self):
        self.check_in_time = datetime.now()
        print("Checked in at:", self.check_in_time.strftime("%Y-%m-%d %H:%M:%S"))

    def check_out(self):
        self.check_out_time = datetime.now()
        print("Checked out at:", self.check_out_time.strftime("%Y-%m-%d %H:%M:%S"))

    def worked_hours(self):
        if self.check_in_time and self.check_out_time:
            delta = self.check_out_time - self.check_in_time
            return delta.total_seconds() / 3600
        return 0
