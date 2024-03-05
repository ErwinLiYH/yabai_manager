# Yabai manager

A simple python program to show basic status of [Yabai](https://github.com/koekeishiya/yabai) WM in status bar with yabai and skhd configuration.

With multiple display:

`|<index in display of current space>|<index in total of current space>|<float or bsp of current space>|`

![](./imgs/Screenshot%202024-03-05%20at%2018.46.25.png)

With single display:

`|<index of current space>|<float or bsp of current space>|`

![](./imgs/Screenshot%202024-03-05%20at%2018.45.01.png)

## install

1. Install Python
2. Install [Yabai](https://github.com/koekeishiya/yabai)
3. Install [skhd](https://github.com/koekeishiya/skhd)
4. Install the configs and Yabai manager

    ```bash
    git clone git@github.com:ErwinLiYH/yabai_manager.git
    cd yabai_manager
    pip install rumps (to build status bar APP)
    # Change the first line of yabai_manager.py and full_screen_all_windows_in_space.py
    # to #!/usr/bin/env <your python program's path>
    ./install.sh
    ```

    You can select install mode, `link` (make soft link of all files to ~) or `copy` (copy all files to ~)

    If you want to customize it, `link` mode is recommended.

## Settings

**Key binds:**

1. `option - p`: toggle focused window to pip (picture in picture)
2. `option - f`: toggle focused window to float and center it

...

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