from pynput import keyboard
from timer import Timer # Class handles timer and display
from session import Session

session = Session()
timer = Timer(session)

app_is_running = True # Check if the app is running.

# controls
def control(event_type):
    global app_is_running

    if event_type == keyboard.Key.space:
        timer.timer_control()

    elif event_type == keyboard.Key.esc:
        timer.end_timer_session()
        app_is_running = False
        return False

if __name__ == '__main__':

    listener = keyboard.Listener(on_press=control)
    listener.start()

    while app_is_running:
        timer.timer_counting()