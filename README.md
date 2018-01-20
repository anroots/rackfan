# rackfan

A fan controller script for the NZXT Grid+ v2 USB fan controller.

Meant for mainly personal use; work in progress.

## Usage

```bash
pip install requirements.txt
cd src
python3 rackfan.py --help 
```

## Use Case

This script runs in a Raspberry Pi, in a standard 19' rack.
The rack has cooling fans connected to a Grid+ controller, that
normally run in  quiet/slow mode. Raspberry Pi monitors the ambient
temperature inside the rack and spins the fans into a faster mode as needed.

# License

The main Grid controller class is borrowed from https://github.com/akej74/grid-control
hence the license is GPLv3.