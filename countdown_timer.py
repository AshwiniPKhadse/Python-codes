import time

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        #to take a pause not start the coundown instantly
        time.sleep(1)
        seconds -= 1
    print("Hey... Stop Stop Stop,Time's up!")

# Set the countdown duration in seconds
countdown_duration = int(input())

# Start the countdown
countdown(countdown_duration)
