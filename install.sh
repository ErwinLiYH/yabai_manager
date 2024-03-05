#!/bin/bash

# Define relative paths
CONFIG_DIR="./config"
MANAGER_DIR="./manager"

# Installation function
install_file() {
    src=$1
    dest=$2
    method=$3 # link or copy

    # Check if the target file exists
    if [ -e "$dest" ]; then
        echo "$dest already exists."
        read -p "Do you want to backup? (y/n): " answer
        if [ "$answer" == "y" ]; then
            backup="${dest}.backup"
            echo "Backing up $dest to $backup"
            cp -a "$dest" "$backup"
        fi
    fi

    # Install the file based on the chosen method: symbolic link or copy
    if [ "$method" == "link" ]; then
        echo "Creating a symbolic link from $src to $dest"
        ln -sfn "$(pwd)/$src" "$dest"
    elif [ "$method" == "copy" ]; then
        echo "Copying the file from $src to $dest"
        cp -a "$src" "$dest"
    fi
}

# Ask the user for the installation method
read -p "Choose the installation method (type 'link' or 'copy'): " method

if [ "$method" != "link" ] && [ "$method" != "copy" ]; then
    echo "Invalid installation method. Exiting the script."
    exit 1
fi

# Install configuration files
install_file "$CONFIG_DIR/.skhdrc" "$HOME/.skhdrc" "$method"
install_file "$CONFIG_DIR/.yabairc" "$HOME/.yabairc" "$method"

# Install manager application files
install_file "$MANAGER_DIR/full_screen_all_windows_in_space.py" "$HOME/full_screen_all_windows_in_space.py" "$method"
install_file "$MANAGER_DIR/utils.py" "$HOME/utils.py" "$method"
install_file "$MANAGER_DIR/yabai_manager.py" "$HOME/yabai_manager.py" "$method"
