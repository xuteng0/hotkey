#!/bin/bash

# Load the LOCK_FILE path from config.json
CONFIG_FILE="config.json"
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: The configuration file $CONFIG_FILE does not exist."
    exit 1
fi

# Load the LOCK_FILE path from config.json
LOCK_FILE=$(jq -r '.lock_file_path' "$CONFIG_FILE")
if [ -z "$LOCK_FILE" ]; then
    echo "Error: lock_file_path is not set in $CONFIG_FILE."
    exit 1
fi

# Check if the script is already running
if [ -f "$LOCK_FILE" ]; then
    echo "Error: $PYTHON_SCRIPT is already running."
    exit 1
fi

# load the PYTHON_SCRIPT path from config.json
PYTHON_SCRIPT=$(jq -r '.python_script_path' "$CONFIG_FILE")
if [ -z "$PYTHON_SCRIPT" ]; then
    echo "Error: python_script_path is not set in $CONFIG_FILE."
    exit 1
fi

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: The script $PYTHON_SCRIPT does not exist."
    exit 1
fi

SCREEN_SESSION_NAME=$(jq -r '.screen_session_name' "$CONFIG_FILE")
if [ -z "$SCREEN_SESSION_NAME" ]; then
    echo "Error: screen_session_name is not set in $CONFIG_FILE."
    exit 1
fi

# Start a new screen session in detached mode
screen -dmS "$SCREEN_SESSION_NAME"

# Run the Python script in the screen session
screen -S "$SCREEN_SESSION_NAME" -X stuff "python $PYTHON_SCRIPT\n"

# Attach to the screen session
screen -r "$SCREEN_SESSION_NAME"

echo "Python script is running in screen session '$SCREEN_SESSION_NAME'"
