#!/bin/bash

# Define relative paths
CONFIG_DIR="./config"
MANAGER_DIR="./manager"

# python script dictionary
PY_DIR="$HOME/yabai_manager"

# Installation function
install_file() {
    src=$1
    dest=$2
    method=$3 # link or copy

    # Check if the target file exists
    if [ -e "$dest" ]; then
        echo "$dest already exists."
        read -p "Do you want to backup? (y/n): " answer
        if [ "$answer" == "y" ] || [ -z "$answer" ]; then
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

update_python_path() {
    new_path=$1
    file=$2
    if [ ! -f "$file" ]; then
        echo "File does not exist: $file"
        return 1
    fi
  sed -i "" "1s|#\!/usr/bin/env .*|#\!/usr/bin/env $new_path|" "$file"
}

# set python environment
PY=$(which python3)
echo "Do you want to use this python environemnt?"
read -p "$PY (y/n): " answer
if [ "$answer" == "n" ]; then
    read -p "Enter the path to the python environment: " PY
fi
echo “Using $PY as the python environment.”

$PY -c "import rumps" 2> /dev/null
if [ $? -eq 0 ]; then
    echo "rumps is already installed"
else
    read -p "rumps is not installed, install now? (y/n): " answer
    if [ "$answer" == "y" ] || [ -z "$answer" ]; then
        $PY -m pip install rumps
    else
        echo "Skipping the installation of rumps."
    fi
fi

# Install configuration files
read -p "Do you want to install config files(.skhdrc & .yabairc)? (y/n): " answer
if [ "$answer" == "y" ] || [ -z "$answer" ]; then
    install_file "$CONFIG_DIR/.skhdrc" "$HOME/.skhdrc" "$method"
    install_file "$CONFIG_DIR/.yabairc" "$HOME/.yabairc" "$method"
else
    echo "Skipping the installation of configuration files."
fi

# Install manager application files
mkdir -p "$PY_DIR"
install_file "$MANAGER_DIR/utils.py" "$PY_DIR/utils.py" "$method"

update_python_path "$PY" "$MANAGER_DIR/yabai_manager.py"
install_file "$MANAGER_DIR/yabai_manager.py" "$PY_DIR/yabai_manager.py" "$method"

update_python_path "$PY" "$MANAGER_DIR/toggle_space_layout.py"
install_file "$MANAGER_DIR//toggle_space_layout.py" "$PY_DIR/toggle_space_layout.py" "$method"

update_python_path "$PY" "$MANAGER_DIR/minimize_all_windows_in_space_except_focused.py"
install_file "$MANAGER_DIR/minimize_all_windows_in_space_except_focused.py" "$PY_DIR/minimize_all_windows_in_space_except_focused.py" "$method"

update_python_path "$PY" "$MANAGER_DIR/deminimize_all_windows_in_space_foucus_original.py"
install_file "$MANAGER_DIR//deminimize_all_windows_in_space_foucus_original.py" "$PY_DIR/deminimize_all_windows_in_space_foucus_original.py" "$method"