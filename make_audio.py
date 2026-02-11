from moviepy import VideoFileClip
import os

# Create the assets folder if it doesn't exist yet
if not os.path.exists("assets"):
    os.makedirs("assets")

# 1. Load your video (Make sure the name matches your file!)
video = VideoFileClip("")

# 2. Extract and save the audio into the assets folder
video.audio.write_audiofile("assets/music.mp3")

print("✅ Success! Your music.mp3 is now in the assets folder.")