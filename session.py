
from datetime import datetime, timedelta, timezone

class Session:
    def __init__(self, controller):
        self.controller = controller
        self.session_dict = {
            'SID_1': {'start_time': '11:02:44', 'end_time': '11:02:47', 'date_of_session': 'October 2, 2026',
                      'total_time': 2},
            'SID_2': {'start_time': '11:02:44', 'end_time': '11:02:47', 'date_of_session': 'October 2, 2026',
                      'total_time': 2},
            'SID_3': {'start_time': '11:02:44', 'end_time': '11:02:47', 'date_of_session': 'October 3, 2026',
                      'total_time': 2},
            'SID_4': {'start_time': '11:02:44', 'end_time': '11:02:47', 'date_of_session': 'October 3, 2026',
                      'total_time': 2},
        }
        self.session_id_counter = 4
        self.date_today = datetime.now(timezone.utc).astimezone().strftime("%B %d, %Y")
        self.formatted_date_yesterday = ""
        self.prefix = "SID"
        self.total_session_today = 0
        self.total_session_yesterday = 0
        self.total_session_all = 0

    # create session
    def create_session(self,date_of_session, start, end, duration):
        print(self.date_today)
        session_id = self.session_id_counter + 1

        new_id = f"{self.prefix}_{session_id}"

        self.session_dict[new_id] = {
            "start_time": start,
            "end_time": end,
            "date_of_session": date_of_session,
            "total_time": int(duration)
        }
        self.session_id_counter = session_id
        print("Session Saved")

    # delete session
    def delete_session(self):
        print("==========================")
        print(f"[BACKSPACE Pressed] System are checking the session...")
        if len(self.session_dict) != 0:
            self.display_session()
            selected_key = self.controller.check_user_input(self.session_dict)

            if selected_key != None:
                deleted_key = f"{self.prefix}_{selected_key}"
                if deleted_key in self.session_dict:
                    del self.session_dict[deleted_key]
                    print("Successfully deleted the Session")
                    self.display_session()
            else:
                print(f"[Cancel Deletion] Exiting now...")
                self.display_session()

        else:
            print(f"\nNo available session to delete. Press 'SPACE' to start")
            print("==========================")


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

    def display_session(self):
        selected_display = self.controller.display_session_input()

        if selected_display == '1':
            self.show_today_session()
        elif selected_display == '2':
            self.show_yesterday_session()
        else:
            self.show_all_session()

    def check_session_date(self, session_date):
        date_obj = datetime.strptime(self.date_today, "%B %d, %Y")
        yesterday_session_date = date_obj - timedelta(days=1)
        self.formatted_date_yesterday = yesterday_session_date.strftime("%B %d, %Y").replace(" 0", " ")

        if self.date_today == session_date:
            date_display = "Today"
        elif self.formatted_date_yesterday == session_date:
            date_display = "Yesterday"
        else:
            date_display = session_date

        return date_display

    def show_today_session(self):
        self.total_session_today = 0
        number_of_today_session = 0
        print("==========================")
        print("LIST OF TODAY's SESSION")
        print("__________________________")
        for x in self.session_dict:
            get_duration = self.session_dict[x]["total_time"]
            display_duration = self.time_formatter(get_duration)
            session_date = self.session_dict[x]["date_of_session"]
            session_remarks = self.check_session_date(session_date)
            if session_date == self.date_today:
                print(f"Session ID: {x}\n"
                      f"Date: {session_remarks}\n"
                      f"Start Time: {self.session_dict[x]["start_time"]}\n"
                      f"End Time: {self.session_dict[x]["end_time"]}\n"
                      f"Session Duration: {display_duration}\n"
                      f"___________________________")
                number_of_today_session +=1
                self.total_session_today = self.today_session_calculation(get_duration)

        if number_of_today_session == 0:
            print(f"No sessions recorded today.")

        else:
            print(f"Total Session Duration: {self.time_formatter(self.total_session_today)}")

        print("==========================")


    def show_yesterday_session(self):
        self.total_session_yesterday = 0
        number_of_yesterday_session = 0
        print("==========================")
        print("LIST OF YESTERDAY's SESSION")
        print("__________________________")
        for x in self.session_dict:
            get_duration = self.session_dict[x]["total_time"]
            display_duration = self.time_formatter(get_duration)
            session_date = self.session_dict[x]["date_of_session"]
            session_remarks = self.check_session_date(session_date)

            if self.formatted_date_yesterday == session_date:
                print(f"Session ID: {x}\n"
                      f"Date: {session_remarks}\n"
                      f"Start Time: {self.session_dict[x]["start_time"]}\n"
                      f"End Time: {self.session_dict[x]["end_time"]}\n"
                      f"Session Duration: {display_duration}\n"
                      f"___________________________")
                number_of_yesterday_session += 1
                self.total_session_yesterday = self.yesterday_session_calculation(get_duration)

        if number_of_yesterday_session == 0:
            print(f"No sessions recorded yesterday.")
        else:
            print(f"Total Session Duration: {self.time_formatter(self.total_session_yesterday)}")

        print("==========================")


    def show_all_session(self):
        self.total_session_all = 0
        print("==========================")
        print("LIST OF All SESSION")
        print("__________________________")
        if len(self.session_dict) != 0:
            for x in self.session_dict:
                get_duration = self.session_dict[x]["total_time"]
                display_duration = self.time_formatter(get_duration)
                session_date = self.session_dict[x]["date_of_session"]

                session_remarks = self.check_session_date(session_date)
                print(f"Session ID: {x}\n"
                      f"Date: {session_remarks}\n"
                      f"Start Time: {self.session_dict[x]["start_time"]}\n"
                      f"End Time: {self.session_dict[x]["end_time"]}\n"
                      f"Session Duration: {display_duration}\n"
                      f"___________________________")
                self.total_session_all = self.all_session_calculation(get_duration)

            display_consumed_time = self.time_formatter(self.total_session_all)
            print(f"All Session Duration: {display_consumed_time}")

        else:
            print(f"There's no session as of this moment....")
        print("==========================")

# session calculation

    def today_session_calculation(self, session_today):
        return self.total_session_today + session_today

    def yesterday_session_calculation(self, session_yesterday):

        return self.total_session_yesterday + session_yesterday

    def all_session_calculation(self, all_session):
        return self.total_session_all + all_session