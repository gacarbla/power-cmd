#!/bin/bash

if [ "$(id -un)" != "root" ] && [ -z "${ANDROID_ROOT}" ]; then
    echo "This script must be run as root on a Linux system or in Termux" 1>&2
    exit 1
fi

echo "Warning: This script does not support the current Linux distribution and may not work correctly. Are you sure you want to continue? (Y/N)"
read -r continue_script

if [[ ! "$continue_script" =~ ^[Yy]$ ]]; then
    echo "Process canceled."
    exit 1
fi

if [ ! -z "${ANDROID_ROOT}" ]; then
    pkg update || { echo "Failed to update packages in Termux." >&2; exit 1; }
else
    if [ -x "$(command -v apt-get)" ]; then
        apt-get update || { echo "Failed to update packages in Linux." >&2; exit 1; }
    elif [ -x "$(command -v pacman)" ]; then
        pacman -Syu --noconfirm || { echo "Failed to update packages in Linux." >&2; exit 1; }
    else
        echo "No compatible package manager detected (apt or pacman)." >&2
        exit 1
    fi
fi

if [ ! -z "${ANDROID_ROOT}" ]; then
    pkg install -y python || { echo "Failed to install Python in Termux." >&2; exit 1; }
else
    if [ -x "$(command -v apt-get)" ]; then
        apt-get install -y python3 || { echo "Failed to install Python in Linux." >&2; exit 1; }
    elif [ -x "$(command -v pacman)" ]; then
        pacman -S --noconfirm python || { echo "Failed to install Python in Linux." >&2; exit 1; }
    else
        echo "No compatible package manager detected (apt or pacman)." >&2
        exit 1
    fi
fi

if [ -x "$(command -v python3)" ]; then
    echo "Python 3 installed successfully."
elif [ -x "$(command -v python)" ]; then
    echo "Python 2 installed successfully."
else
    echo "Python installation failed!" >&2
    exit 1
fi