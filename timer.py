import time

class Timer:
    def __init__(self):
        self.is_counting = False # Check if the timer is counting
        self.session_start_time = 0 # Check if the app is running.
        self.elapsed_time = 0 # Start time stamp
        self.accumulated_time_session = [] # total accumulated time


    # timer and display
    def timer_display(self):
        if self.is_counting:
            total_time = sum(self.accumulated_time_session) + self.elapsed_time

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
            self.timer_display()

    def timer_control(self):
        self.is_counting = not self.is_counting
        if self.is_counting:
            print(f"\n[Spacebar Pressed] System is now: RUNNING")
            self.session_start_time = time.perf_counter()

        else:
            # Save each accumulated session to the list
            self.accumulated_time_session.append(self.elapsed_time)
            print(f"Accumulated time = {self.accumulated_time_session}")
            print(f"\n[Spacebar Pressed] System is now: PAUSED")
            print("=====================")
            self.elapsed_time = 0

    def end_timer_session(self):
        if self.is_counting:
            print("Save while running")
            self.accumulated_time_session.append(int(self.elapsed_time))
            print(f"Accumulated time = {self.accumulated_time_session}")
            self.is_counting = False
        else:
            pass

        print(f"Total Accumulated time is {sum(self.accumulated_time_session)}")
        self.elapsed_time = 0
        print('App terminated')
