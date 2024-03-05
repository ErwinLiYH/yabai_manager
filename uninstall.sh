#!/bin/bash

files=(
  ".skhdrc"
  ".yabairc"
  "full_screen_all_windows_in_space.py"
  "utils.py"
  "yabai_manager.py"
)

uninstall_file() {
    file=$1
    if [ -e "$HOME/$file" ]; then
        read -p "Do you want to remove $file from the home directory? (y/n): " answer
        if [ "$answer" == "y" ]; then
            rm -rf "$HOME/$file"
            echo "$file has been removed."
        else
            echo "Skipping $file."
        fi
    else
        echo "$file does not exist in the home directory."
    fi
}

for file in "${files[@]}"; do
    uninstall_file "$file"
done

echo "Uninstallation complete."
