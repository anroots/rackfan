# rackfan

A fan controller script for the NZXT Grid+ v2 USB fan controller.

Mainly for personal use; work in progress.

## Usage

```bash
$ pip install requirements.txt
$ cd src
$ python3 rackfan.py --help
usage: rackfan.py [-h] [-v] [-s SERIAL] [-f FAN] [-p PERCENTAGE] [-o]

This software controls fans connected to NZXT GRID+ v2 fan controller

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show version information
  -s SERIAL, --serial SERIAL
                        specify the serial port to use
  -f FAN, --fan FAN     specify a fan number to control (used with -o)
  -p PERCENTAGE, --percentage PERCENTAGE
                        set fan speed to x percent (used with -o)
  -o, --one-off         run a one-off command and exit (needs extra arguments)

```

## Use Case

This script runs in a Raspberry Pi, in a standard 19' rack. The rack has cooling fans connected to a Grid+ controller,
that normally run in  quiet/slow mode.

Raspberry Pi monitors the ambient temperature inside the rack and spins the fans into a faster mode as needed.

# License

The main Grid controller class is borrowed from https://github.com/akej74/grid-control, hence the license is GPLv3.