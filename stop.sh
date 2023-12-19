#!/bin/bash

# Define the name of the screen session
SCREEN_SESSION_NAME="chrome_video_pause_hotkey"

# Check if any screen session exists
if screen -list | grep -q "$SCREEN_SESSION_NAME"; then
    # Get a list of all matching screen sessions
    SESSIONS=$(screen -list | grep "$SCREEN_SESSION_NAME" | awk -F '.' '{print $1}')

    # Loop through each matching session and terminate it
    for SESSION in $SESSIONS; do
        # Send Ctrl+C to the session (assuming it will stop the running process)
        screen -S "$SESSION" -X stuff $'\003'

        # Wait for a moment to allow the process to terminate
        sleep 1

        # Quit the screen session
        screen -S "$SESSION" -X quit

        echo "Screen session '$SESSION' has been terminated."
    done
else
    echo "Error: No screen sessions named '$SCREEN_SESSION_NAME' were found."
fi
