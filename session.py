class Session:
    def __init__(self):
        self.session_dict = {}
        self.session_id_counter = 0


    def create_session(self, start, end, duration):

        session_id = self.session_id_counter + 1
        prefix = "SID"
        new_id = f"{prefix}_{session_id}"

        self.session_dict[new_id] = {
            "start_time": start,
            "end_time": end,
            "total_time": int(duration)
        }
        self.session_id_counter = session_id
        print("Session Saved")

    def time_formatter(self, total_time):
        value = 60
        seconds = total_time % value
        minutes_count = total_time // value
        minutes = minutes_count % value
        hours = minutes_count // value

        display_time = self.time_display(seconds, minutes, hours)

        return display_time

    def time_display(self, seconds, minutes, hours):

        if 0 < hours:
            display_hours = f"{hours} hour" if hours == 1 else f"{hours} hours"
        else:
            display_hours = ""

        if 0 < minutes:
            if hours == 0:
                display_minutes = f"{minutes} minute" if minutes == 1 else f"{minutes} minutes"
            elif seconds == 0:
                display_minutes = f"and {minutes} minute" if minutes == 1 else f"and {minutes} minutes"
            else:
                display_minutes = f"{minutes} minute" if minutes == 1 else f"{minutes} minutes"
        else:
            display_minutes = ""

        if 0 < seconds:
            if 0 < minutes or 0 < hours:
                display_seconds = f"and {seconds} second" if seconds == 1 else f"and {seconds} seconds"
            else:
                display_seconds = f"{seconds} second" if seconds == 1 else f"{seconds} seconds"
        elif minutes > 0 or hours > 0:
            display_seconds = ""
        else:
            display_seconds = "0 seconds"

        # Separator is only needed if seconds are valid AND a higher unit (minutes or hours) exists
        display_separator_seconds = ""
        if hours != 0 and minutes != 0 or hours != 0 or minutes != 0:
            display_separator_seconds = " "

        # Separator is only needed if minutes are valid AND hours exist
        display_separator_minutes = ""
        if hours != 0 and minutes != 0 and seconds != 0:
            display_separator_minutes = ", "
        elif hours != 0 and minutes != 0:
            display_separator_minutes = " "


        display = f"{display_hours}{display_separator_minutes}{display_minutes}{display_separator_seconds}{display_seconds}"
        return display

    def display_all_session(self):
        for x in self.session_dict:
            get_duration = self.session_dict[x]["total_time"]
            display_duration = self.time_formatter(get_duration)
            print("==========================")
            print(f"Session ID: {x}\n"
                  f"Start Time: {self.session_dict[x]["start_time"]}\n"
                  f"End Time: {self.session_dict[x]["end_time"]}\n"
                  f"Session Duration: {display_duration}")

        print("___________________________")
        total_consumed_time = sum(item["total_time"] for item in self.session_dict.values())
        display_consumed_time = self.time_formatter(total_consumed_time)
        print(f"Total Session Duration: {display_consumed_time}")
        print("==========================")