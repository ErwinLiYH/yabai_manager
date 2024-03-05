#!/bin/bash

files=(
  ".skhdrc"
  ".yabairc"
  "yabai_manager/toggle_space_layout.py"
  "yabai_manager/utils.py"
  "yabai_manager/yabai_manager.py"
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

rm -rf "$HOME/yabai_manager"

echo "Uninstallation complete."
