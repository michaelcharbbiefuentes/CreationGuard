import time
from datetime import datetime, timezone

class Timer:
    def __init__(self, session):
        self.session = session
        self.is_counting = False # Check if the timer is counting
        self.session_start_time = 0 # session starting time
        self.elapsed_time = 0 #total elapsed time
        self.session_start_datetime = 0 # time stamp when session started
        self.session_date = 0 # date of session

    # check current time
    def check_current_time(self):
        local_datetime = datetime.now(timezone.utc).astimezone()
        date_today = local_datetime.strftime("%B %d, %Y")
        time_now = local_datetime.strftime("%I:%M:%S")
        self.session_date = date_today

        return time_now

    # timer and display
    def timer(self):
        if self.is_counting:
            total_time = self.elapsed_time
            value = 60
            seconds = total_time % value
            minutes_count = total_time // value
            minutes = minutes_count % value
            hours = minutes_count // value

            seconds_value = f"{seconds:02d}"
            minutes_value = f"{minutes:02d}"
            hours_value = f"{hours:02d}"

            print(f"Elapsed Time: {hours_value}:{minutes_value}:{seconds_value}")

        else:
            pass

    def timer_counting(self):
        delay = 1
        if self.is_counting:
            time.sleep(delay)
            time_difference = time.perf_counter() - self.session_start_time
            self.elapsed_time = int(time_difference)
            self.timer()

    def timer_control(self):
        self.is_counting = not self.is_counting
        if self.is_counting:
            print(f"\n[Spacebar Pressed] System is now: RUNNING")
            self.session_start_time = time.perf_counter()
            self.session_start_datetime = self.check_current_time() #save start time

        else:
            # Create and Save Session
            print(f"\n[Spacebar Pressed] System is now: STOPPED")
            self.save_session()
            self.elapsed_time = 0
            print("=====================")

    def end_timer_session(self):
        if self.is_counting:
            self.save_session()
            self.is_counting = False
        else:
            pass

        self.session.display_session()
        self.elapsed_time = 0
        print('App terminated')

    def save_session(self):
        self.session.create_session(self.session_date, self.session_start_datetime, self.check_current_time(), self.elapsed_time)

