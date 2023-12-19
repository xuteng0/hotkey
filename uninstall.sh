#!/bin/bash

# File containing the list of requirements
REQ_FILE="requirements.txt"

# Check if the requirements file exists
if [ ! -f "$REQ_FILE" ]; then
    echo "Error: $REQ_FILE does not exist."
    exit 1
fi

# Read each line in the requirements file and uninstall the package
while IFS= read -r package; do
    echo "Uninstalling $package..."
    pip uninstall -y "$package"
done < "$REQ_FILE"

echo "Uninstallation complete."
