#next task
#create a session.


import time
from pynput import keyboard

is_counting = "" # Check if the timer is counting
app_is_running = True # Check if the app is running.
start_count = 0 # Start time stamp
elapsed_time = 0 # total time elapsed
accumulated_time_session = [] # total accumulated time

#timer and display
def timer_display():
    global elapsed_time
    total_time = sum(accumulated_time_session) + elapsed_time
    value = 60
    seconds = total_time % value
    minutes_count = total_time // value
    minutes = minutes_count % value
    hours = minutes_count // value
    seconds_value = f"{seconds:02d}"
    minutes_value = f"{minutes:02d}"
    hours_value = f"{hours:02d}"
    print(f"Elapsed Time: {hours_value}:{minutes_value}:{seconds_value}")

# create a session
def create_session():
    pass

# controls
def control(event_type):
    global is_counting
    global app_is_running
    global start_count
    global elapsed_time

    if event_type == keyboard.Key.space:
        is_counting = not is_counting
        state = "RUNNING" if is_counting else "PAUSED"


        if state == "RUNNING":
            elapsed_time = 0
            print(f"\n[Spacebar Pressed] System is now: {state}")
            start_count = time.perf_counter()
            return True

        else:
            #save accumulated time session to list
            accumulated_time_session.append(elapsed_time)
            print(f"Accumulated time = {accumulated_time_session}")
            print(f"\n[Spacebar Pressed] System is now: {state}")
            print("=====================")
            return True


    elif event_type == keyboard.Key.esc:
        if is_counting:
            print("Save while running")
            accumulated_time_session.append(int(elapsed_time))
            print(f"Accumulated time = {accumulated_time_session}")
        else:
            pass

        print(f"Total Accumulated time is {sum(accumulated_time_session)}")
        print('App terminated')
        app_is_running = False
        return False


if __name__ == '__main__':

    listener = keyboard.Listener(on_press=control)
    listener.start()

    while app_is_running:
        if is_counting:
            delay = 1
            time.sleep(delay)
            time_difference = time.perf_counter() - start_count
            elapsed_time = int(time_difference)
            timer_display()