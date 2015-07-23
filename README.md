# zrpr
**zrpr** is a **z**ypper tool to **r**emove all **p**ackages from a specific **r**epository. I know, it's a horrible name.

Since zypper doesn't remove the repo packages when you do **zypper rr** I made this script. Please notice that **this script won't issue any commands**, it will only **print the command line** to remove all packages.

## Usage

Let's say you want to remove **games** repository from your beautiful no-gaming openSUSE, but you also want to remove all packages from this repo. Instead of typing all of the packages in the command line, just run **zrpr.py**. It will ask you this:

> Hello there, my fellow friend! Please, tell me, which repository are you removing today?

And you'll answer, since you're a nice person.

> games

And it will say:

> sudo zypper rm libIL1 libSDL2-2_0-0 libSDL_image-1_2-0 libSDL_net-1_2-0 libSDL_sound-1_0-1 libluajit-5_1-2 libphysfs1 xboard

*because these are my packages installed from **games** repo*

Just copy and paste these in your terminal, and be happy! :+1: