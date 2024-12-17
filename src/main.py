from sound_detection import detect_can_opening
from direction_finder import find_sound_direction
from motor_control import aim_and_fire
from mock_data import get_mock_sound_data

def main():
    # Simulate getting sound data
    sound_data = get_mock_sound_data()
    
    # Detect if the sound corresponds to a can opening
    if detect_can_opening(sound_data):
        print("Can opening detected!")

        # Find the direction of the sound
        direction = find_sound_direction(sound_data)
        print(f"Sound detected from direction: {direction}°")

        # Aim and fire at the sound direction
        aim_and_fire(direction)
    else:
        print("No can opening detected.")

if __name__ == "__main__":
    main()
