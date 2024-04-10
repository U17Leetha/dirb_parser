#!/bin/bash

# Install Python if not already installed
if ! command -v python &> /dev/null; then
    echo "Python is not installed. Installing Python..."
    sudo apt-get update
    sudo apt-get install -y python
fi

# Install DIRB if not already installed
if ! command -v dirb &> /dev/null; then
    echo "DIRB is not installed. Installing DIRB..."
    sudo apt-get update
    sudo apt-get install -y dirb
fi

# Copy the Python script to /usr/local/bin with the name dirb-parser
sudo cp dirb_parser.py /usr/local/bin/dirb-parser

# Make the script executable
sudo chmod +x /usr/local/bin/dirb-parser

echo "dirb-parser has been installed. You can now run 'dirb-parser' from any directory."
