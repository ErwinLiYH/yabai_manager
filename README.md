# Yabai manager

A simple python program to show basic status of [Yabai](https://github.com/koekeishiya/yabai) WM in status bar.

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

    This APP need a python environment, if you don't want to use system python env, you should create a new virtual Python environment before running `install.sh`, and select the Python interpreter path in the environment when running `install.sh`.

    ```bash
    git clone git@github.com:ErwinLiYH/yabai_manager.git
    cd yabai_manager
    ./install.sh
    ```

    You can select install mode, `link` (make soft link of all files to ~) or `copy` (copy all files to ~). If you want to customize it, `link` mode is recommended.

    The install script will remind you to backup old config(.skhdrc & .yabairc) if you have, so don't worry about losting config file.

    You can select whether to use my config file when install, if you chooes not to install my config file, you can build you own config files integrated with the manager according to the last section.

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