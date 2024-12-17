import time
from respeaker import Microphone


mic = Microphone()

while True:
    # Capture sound data from the array
    data = mic.listen()
    direction = mic.get_direction(data)
    
    print(f"Sound direction: {direction} degrees")
    time.sleep(0.1)
