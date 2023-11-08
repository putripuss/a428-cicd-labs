#!/usr/bin/env sh

# Check if .pidfile exists
if [ ! -f .pidfile ]; then
    echo "Error: .pidfile not found. Exiting..."
    exit 1
fi

# Get PID from .pidfile and terminate the process
PID=$(cat .pidfile)
kill $PID

# Check if the process was terminated successfully
if [ $? -eq 0 ]; then
    echo "Process with PID $PID terminated successfully."
else
    echo "Error: Failed to terminate process with PID $PID."
fi
