# Yabai manager

A simple python program to show basic status of [Yabai](https://github.com/koekeishiya/yabai) WM in status bar.

![](./imgs/Screenshot%202024-03-10%20at%2019.49.38.png)

This program include:

1. Three high-level interfaces to control Yabai's behavior
    1. Minimize all windows in the space (except the focused window)
    2. Deminimize all windows in the space (then refocus to original window)
    3. Toggle space's layout between bsp and float(, and maximize all windows after transferred to float layout)
2. A manager in GUI: shows the information of Yabai WM and calls these high-level interfaces
3. A manager in CLI: calls these high-level interfaces
4. Default configuration files(.skhdrc & .yabairc) integrated with the manager

With multiple display:

`|<space index in display>:<space count in display>|<space index in total>:<space count in total>|<float('F'loat) or bsp('T'ile) of current space>|`

![](./imgs/Screenshot%202024-03-05%20at%2018.46.25.png)

With single display:

`|<space index>:<space count>|<float('F'loat) or bsp('T'ile) of current space>|`

![](./imgs/Screenshot%202024-03-05%20at%2018.45.01.png)

## install

1. Install Python
2. Install [Yabai](https://github.com/koekeishiya/yabai)
3. Install [skhd](https://github.com/koekeishiya/skhd)
4. Install the configs and Yabai manager

    This app requires a Python environment. If you prefer not to use the system's Python environment, you should create a new virtual Python environment.

    ```bash
    git clone git@github.com:ErwinLiYH/yabai_manager.git
    cd yabai_manager

    pip install -e .

    # optional
    cp default_config/.skhdrc ~/.skhdrc
    cp default_config/.yabairc ~/.yabairc

    #or

    ln -s default_config/.skhdrc ~/.skhdrc
    ln -s default_config/.yabairc ~/.yabairc
    ```

## Settings

**Key binds:**

1. `option - p`: toggle focused window to pip (picture in picture)
2. `option - t`: toggle focused window between \<float and center\>/bsp
3. `option - f`: toggle focused window to full screen(by grid command, used in float layout)
4. `option - z`: toggle focused window to zoom full screen(used in bsp layout)
5. `shift + cmd - t`: toggle layout of screen
    
    float -> bsp : change layout
    bsp -> float : change layout and full screen all windows

6. `shift + cmd + alt - r`: restart Yabai and manager

## Customize

...