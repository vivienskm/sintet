import time

def countdown_timer(duration):
    while duration >= 0:
        minutes, seconds = divmod(duration, 60)
        timer = f"{minutes:02d}:{seconds:02d}"
        print(timer, end="\r")
        time.sleep(1)
        duration -= 1
    print("Countdown complete!")

# Example usage: countdown_timer(120) for a 2-minute countdown
