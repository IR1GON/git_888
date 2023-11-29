import sys
import time
#start in the terminal - 'python main.py 10(number of seconds)'
def print_time(seconds):
    for i in range(seconds):
        print(f"Time: {i + 1} second(s)")
        time.sleep(1)

def main():
    if len(sys.argv) != 2:
        print("Please provide only one argument - an integer representing seconds")
        return

    try:
        seconds = int(sys.argv[1])
        if seconds <= 0:
            print("Please enter a positive integer")
            return
        print_time(seconds)
    except ValueError:
        print("Incorrect number format. Please enter an integer.")

if __name__ == "__main__":
    main()
