# Yabai manager

A simple python program to show basic status of [Yabai](https://github.com/koekeishiya/yabai) WM in status bar  based on [rumps](https://github.com/jaredks/rumps) with some high-level interfaces based on Yabai.

![](./imgs/Screenshot%202024-03-10%20at%2019.49.38.png)

**This program include:**

1. Three high-level interfaces to control Yabai's behavior
    1. Minimize all windows in the space (except the focused window) (and left the focued window)
    2. Deminimize all windows in the space (then refocus to original window)
    3. Toggle space's layout between bsp and float(, and maximize all windows after transferred to float layout)
2. A manager in GUI (in status bar): shows the information of Yabai WM and calls these high-level interfaces
3. A manager in CLI: calls these high-level interfaces
4. Default configuration files(.skhdrc & .yabairc) integrated with the manager

> contents in () are default behavior in status bar, but optional in CLI.

**With multiple display:**

`|<space index in display>:<space count in display>|<space index in total>:<space count in total>|<float('F'loat) or bsp('T'ile) of current space>|`

![](./imgs/Screenshot%202024-03-05%20at%2018.46.25.png)

**With single display:**

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

    # Install manager
    pip install -e .

    # Install default config, optional
    cp -a default_config/.skhdrc ~/.skhdrc
    cp -a default_config/.yabairc ~/.yabairc

    #or
    ln -s $(pwd)/default_config/.skhdrc ~/.skhdrc
    ln -s $(pwd)/default_config/.yabairc ~/.yabairc
    ```

## Usage

**Default key binds:**

1. `option - p`: toggle focused window to pip (picture in picture)
2. `option - t`: toggle focused window between \<float and center\>/bsp
3. `option - f`: toggle focused window to full screen(by grid command, used in float layout)
4. `option - z`: toggle focused window to zoom full screen(used in bsp layout)
5. `option - w`: make focused window to topbest
6. `option - s`: make focused window to normal layer (revert to normal from topbest)
7. `option - a`: make focused window to left-half
8. `option - d`: make focused window to right-half
9. `shift + cmd - t`: toggle layout of screen
    
    float -> bsp : change layout
    
    bsp -> float : change layout and full screen all windows

10. shift + cmd - w: deminimize all windows in space and refocus to original window
11. shift + cmd - s: minimize all unfocused windows in space
12. `shift + cmd + alt - r`: restart Yabai and manager

**GUI interface:**

**CLI interface:**

**Customize status bar:**