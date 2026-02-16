import os
import time

# ASCII characters for different brightness levels
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',']

def print_frame(frame_data):
    """Print a frame to the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print(frame_data)

def create_bad_apple_animation():
    """Create a simple Bad Apple animation in ASCII"""
    
    # Simple animation frames (you can expand this with more frames)
    frames = [
        # Frame 1 - Top part
        """
        ╔════════════════════════════════════╗
        ║                                    ║
        ║           ████████████             ║
        ║         ██████████████████         ║
        ║        ████████████████████        ║
        ║        ████████████████████        ║
        ║        ████████████████████        ║
        ║         ██████████████████         ║
        ║           ████████████             ║
        ║                                    ║
        ╚════════════════════════════════════╝
        """,
        # Frame 2 - Middle part
        """
        ╔════════════════════════════════════╗
        ║                                    ║
        ║             ██████████             ║
        ║           ████████████████         ║
        ║          ██████████████████        ║
        ║          ██████████████████        ║
        ║          ██████████████████        ║
        ║           ████████████████         ║
        ║             ██████████             ║
        ║                                    ║
        ╚════════════════════════════════════╝
        """,
        # Frame 3 - Bottom part
        """
        ╔════════════════════════════════════╗
        ║                                    ║
        ║               ████████             ║
        ║             ██████████████         ║
        ║            ████████████████        ║
        ║            ████████████████        ║
        ║            ████████████████        ║
        ║             ██████████████         ║
        ║               ████████             ║
        ║                                    ║
        ╚════════════════════════════════════╝
        """,
        # Frame 4 - Shrinking
        """
        ╔════════════════════════════════════╗
        ║                                    ║
        ║                ████                ║
        ║              ██████████            ║
        ║             ████████████           ║
        ║             ████████████           ║
        ║             ████████████           ║
        ║              ██████████            ║
        ║                ████                ║
        ║                                    ║
        ╚════════════════════════════════════╝
        """,
        # Frame 5 - Almost gone
        """
        ╔════════════════════════════════════╗
        ║                                    ║
        ║                                    ║
        ║               ██████               ║
        ║              ████████              ║
        ║              ████████              ║
        ║               ██████               ║
        ║                                    ║
        ║                                    ║
        ║                                    ║
        ╚════════════════════════════════════╝
        """,
    ]
    
    print("\n🎵 BAD APPLE ASCII ANIMATION 🎵\n")
    print("Press Ctrl+C to stop\n")
    time.sleep(2)
    
    try:
        while True:
            for frame in frames:
                print_frame(frame)
                time.sleep(0.3)  # Speed of animation
    except KeyboardInterrupt:
        print("\n\n👋 Animation stopped!")

if __name__ == "__main__":
    create_bad_apple_animation()