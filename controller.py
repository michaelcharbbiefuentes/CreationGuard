class Controller:
    def __init__(self):
        self.user_input = ""
        self.is_user_input_valid = False
        self.input_key_id = ""
        self.input_id = None


    def check_user_input(self, dict_of_session):
        self.is_user_input_valid = False
        while not self.is_user_input_valid:
            print("Do you want to delete a session?")
            user_input = str(input("Type 'y' or 'yes' for YES,\n"
                               "Type 'n' or 'no' for NO: ").lower())
            clean_input = user_input.replace(" ", "")
            print(user_input)
            if clean_input == "yes" or clean_input == 'y':
                deleted_key = self.check_input_key(dict_of_session)
                self.is_user_input_valid = True
                return deleted_key
            elif clean_input == "no" or clean_input == 'n':
                self.is_user_input_valid = True
                return None
            else:
                print("Please try again....")
                self.is_user_input_valid = False

    def check_input_key(self, list_of_session):

        is_valid_key = False
        while not is_valid_key:
            print(f"You have {len(list_of_session)} Session ID")
            print(list(list_of_session.keys()))
            print("Please enter the session number you want to delete?")
            self.input_key_id = input(f"Enter a number: ")
            if self.input_key_id.isdigit():
                session_id = f"SID_{self.input_key_id}"
                if session_id in list_of_session:
                    is_valid_key = True
                else:
                    print("Please try again....")
                    is_valid_key = False

            else:
                print("Please try again....")
                is_valid_key = False

        return self.input_key_id

    def display_session_input(self):
        is_valid_key = False
        while not is_valid_key:
            print("Session Display Controls:\n"
                  "[1] Show Today's Session\n"
                  "[2] Show Yesterday's Session\n"
                  "[3] Show All Session\n")
            user_input = input(f"Please enter a number: ")
            self.input_id = user_input.replace(" ", "")
            if self.input_id.isdigit():
                if self.input_id == '1':
                    is_valid_key = True
                elif self.input_id == '2':
                    is_valid_key = True
                elif self.input_id == '3':
                    is_valid_key = True
                else:
                    print("Please try again....")
                    is_valid_key = False
            else:
                print("Please try again....")
                is_valid_key = False
                print(self.input_id)

        return self.input_id