import time
import os

def scroll_prompt(prompt, speed=0.1):
    while True:
        os.system('clear')  # Clear the console
        print(prompt)
        time.sleep(speed)  # Wait for a few seconds
        prompt = prompt[1:] + prompt[0]  # Shift the prompt to the left

# Example usage:

scroll_prompt(input(str()))