from pynput import keyboard
from timer import Timer # Class handles timer and display
from session import Session
from controller import Controller

controller = Controller()
session = Session(controller)
timer = Timer(session)


app_is_running = True # Check if the app is running.

# controls
def control(event_type):
    global app_is_running

    if event_type == keyboard.Key.space:
        timer.timer_control()

    elif event_type== keyboard.Key.backspace:
        if not timer.is_counting:
            session.delete_session()
        else:
            print("=====================")
            print("System is now 'RUNNING', we can't delete a session")
            print("=====================")
    elif event_type == keyboard.Key.esc:
        timer.end_timer_session()
        app_is_running = False
        return False

if __name__ == '__main__':

    listener = keyboard.Listener(on_press=control)
    listener.start()

    # display message
    print("Controls:\n"
          "Press 'SPACE' to start/end the session\n"
          "Press 'BACKSPACE' to delete existing session\n"
          "Press 'ESC' to terminate the app.")

    while app_is_running:
        timer.timer_counting()