[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Static Badge](https://img.shields.io/badge/Python-3.12-green?logo=Python&logoColor=%25230098FF&link=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-3120%2F) ![Static Badge](https://img.shields.io/badge/Website-Jittapatrick-blue?logo=README&logoColor=%23999999&link=https%3A%2F%2Fbit.ly%2Fjittapatrick) ![Static Badge](https://img.shields.io/badge/Github-patrick2544-black?logo=Github&logoColor=%25230098FF&link=https%3A%2F%2Fgithub.com%2FPatrick2544) ![Static Badge](https://img.shields.io/badge/Paypal-donate-purple?logo=Paypal&logoColor=%25230098FF&link=https%3A%2F%2Fpaypal.me%2Fsjpmiles%3Fcountry.x%3DTH%26locale.x%3Dth_TH)



# Conway's Game of Life
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.for more information please [click here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Game of Life Output Example

![วิดีโอไม่มีชื่อ - สร้างด้วย Clipchamp](https://github.com/Patrick2544/Game_of_Life_Python/assets/52234759/bfbbf4be-bbf7-4ffe-bcae-2050315da068)
---

# Rules
The Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (populated and unpopulated, respectively)

The rules of how cells evolve:

        1) Alive cells die if they have fewer than two (underpopulation) or more than three living neighbors (overpopulation).
        2) Alive cells stay alive if they have two or three living neighbors.
        3) Dead cells with exactly three living neighbors become alive (reproduction).

# Getting Started
The project uses [Curses](https://docs.python.org/3/howto/curses.html), which is a library in python. Please Note that Curses might not work well with Windows.

## Curses Installation

For Python 3:

        pip3 install windows-curses

For Python 2:

        pip install window-curses

macOS and linux systems typically includes the curses module in the Python installation.

Check for curses:

        python -c "import curses"

## Set up a python virtual environment

For more details information please [click here](https://docs.python.org/3/library/venv.html)

For Windows:

        python -m venv venv
        venv\Scripts\activate

For macOs and Linux systems:

        python -m venv venv
        source venv/bin/activate

## install Game of Life
install the project in a dedicated Python virtual environment according to the pyproject.toml file

For all systems:

        python -m pip install -e .

## Run Game of Life
Once the project has been installed according to the command above, now you can run a project directly using the following commands

This is the command for the example output at the beginning of this file:

        Game_of_Life -p "Glider Gun" -g 100

other commands can be found in cli.py file

Here is the brief information

set a specific version

        --version 

get a specific pattern:

        -p or --pattern "pattern's name"

get all patterns:

        -a or --all

set a specific life grid view:

        -v or --view "NameView"

set a number of life grid generations

        -g or --gen #number

set frame rate per second

        -f or --fps #number
