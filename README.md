# Yabai manager

A simple program to show basic status of Yabai WM in status bar.

With multiple display:

`|<index in display of current space>|<index in total of current space>|<float or bsp of current space>|`

![](./imgs/Screenshot%202024-03-05%20at%2018.46.25.png)

With single display:

`|<index of current space>|<float or bsp of current space>|`

![](./imgs/Screenshot%202024-03-05%20at%2018.45.01.png)

## install

1. Install Yabai
2. Install skhd
3. Install the configs and Yabai manager

    ```bash
    git clone 
    cd
    ./install.sh
    ```

    You can select install mode, link (make soft link of all files to ~) or copy (copy all files to ~)

## Settings

**Key binds:**

```bash
# toggle single window layout
alt - p : yabai -m window --toggle pip
alt - f : yabai -m window --toggle float --grid 5:5:1:1:3:3
alt - z : yabai -m window --toggle zoom-fullscreen

# toggle space layout
# toggle space to float layout and full screen all windows, then updates manager
shift + cmd - f : yabai -m space --layout float && ~/full_screen_all_windows_in_space.py && echo "u" | nc localhost 22118
# toggle space to bsp layout and updates manager
shift + cmd - t : yabai -m space --layout bsp && echo "u" | nc localhost 22118

# restart yabai (exits manager --> restarts yabai)
shift + cmd + alt - r : echo "q" | nc localhost 22118 && yabai --restart-service
```

## Customize

...