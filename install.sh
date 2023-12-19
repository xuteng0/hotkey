#!/bin/bash

# Path to your requirements.txt file
REQUIREMENTS_FILE="requirements.txt"

# Check if requirements.txt file exists
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "Error: $REQUIREMENTS_FILE does not exist."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Error: Python is not installed."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null
then
    echo "Error: pip is not installed."
    exit 1
fi

# Install requirements using pip
echo "Installing requirements from $REQUIREMENTS_FILE..."
pip3 install -r $REQUIREMENTS_FILE

if [ $? -eq 0 ]; then
    echo "Successfully installed requirements."
else
    echo "Failed to install requirements."
    exit 1
fi
