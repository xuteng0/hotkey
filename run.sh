#!/bin/bash

# Define the name of the screen session and the Python script
SCREEN_SESSION_NAME="chrome_video_pause_hotkey"
PYTHON_SCRIPT="video_pause_shortcut.py"
FLAG_FILE = "/tmp/video_pause_shortcut_script_lock"

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: The script $PYTHON_SCRIPT does not exist."
    exit 1
fi

# Check if the flag file exists
if [ -f "$FLAG_FILE" ]; then
    echo "Error: $PYTHON_SCRIPT is already running."
    exit 1
fi

# Start a new screen session in detached mode
screen -dmS "$SCREEN_SESSION_NAME"

# Run the Python script in the screen session
screen -S "$SCREEN_SESSION_NAME" -X stuff "python $PYTHON_SCRIPT\n"

# Attach to the screen session
screen -r "$SCREEN_SESSION_NAME"

echo "Python script is running in screen session '$SCREEN_SESSION_NAME'"
