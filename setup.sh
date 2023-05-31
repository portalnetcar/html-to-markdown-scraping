#!/bin/bash

# Function to check if a command exists
command_exists () {
    type "$1" &> /dev/null ;
}

# Check Python
if command_exists python3 ; then
    echo "Python 3 is installed"
else
    echo "Python 3 is not installed. Please install it and run this script again."
    exit 1
fi

# Check pip
if command_exists pip3 ; then
    echo "pip3 is installed"
else
    echo "pip3 is not installed. is not installed. Please install it and run this script again."
    exit 1
fi

# Install Python dependencies
pip3 install requests bs4 markdown beautifulsoup4

# Run the Python script
echo "Ready to run your scraping"
