# Yabai manager

A simple python program to show basic status of [Yabai](https://github.com/koekeishiya/yabai) WM in status bar.

![](./imgs/Screenshot%202024-03-06%20at%2000.26.46.png)

This program include:

1. A manager: shows the information of Yabai WM
2. Basic configuration files(.skhdrc & .yabairc) integrated with the manager

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

    This app requires a Python environment. If you prefer not to use the system's Python environment, you should create a new virtual Python environment before running install.sh. Then, select the Python interpreter path from this environment when running install.sh.

    ```bash
    git clone git@github.com:ErwinLiYH/yabai_manager.git
    cd yabai_manager
    ./install.sh
    ```

    You can select the installation mode: link (creates soft links for all files to the home directory ~) or copy (copies all files to the home directory ~). If you wish to customize it, the link mode is recommended.

    The installation script will prompt you to backup your existing configuration files (.skhdrc & .yabairc) if they exist, so there's no need to worry about losing your configuration files.

    You have the option to use my configuration files during the installation. If you choose not to install my configuration files, you can create your own configuration files integrated with the manager, as described in the last section.

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