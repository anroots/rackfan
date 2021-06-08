import argparse
import threading
import serial
import grid, helper
import sys
import time

class RackFan:

    VERSION = '0.1'

    def __init__(self) -> None:

        self.parse_args()

        # Serial communication object
        self.ser = serial.Serial()


        # Object for locking the serial port while sending/receiving data
        self.lock = threading.Lock()

        # Use the specified serial port or default to the first available one
        serial_ports = grid.get_serial_ports()
        self.serial_port = self.args.serial or serial_ports[0]

        # Initialize communication
        self.init_communication()

        if self.args.one_off:
            for fan_number in self.args.fan:
                grid.set_fan(ser=self.ser, fan=fan_number, voltage=grid.calculate_voltage(self.args.percentage), lock=self.lock)
            time.sleep(3)
            print(grid.read_fan_rpm(ser=self.ser,lock=self.lock))
            sys.exit(0)

        self.main_loop()

    def main_loop(self):


        while True:
            time.sleep(2)

    def parse_args(self):

        description="""
        This software controls fans connected to NZXT GRID+ v2 fan controller
        """
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument("-v", "--version", help="show version information", action="store_true")
        parser.add_argument("-s", "--serial", help="specify the serial port to use")
        parser.add_argument("-f", "--fan", action='append', help="specify a fan number to control (used with -o)", type=int)
        parser.add_argument("-p", "--percentage", help='set fan speed to x percent (used with -o)', type=int)
        parser.add_argument("-o","--one-off",help="run a one-off command and exit (needs extra arguments)", action="store_true")

        self.args = parser.parse_args()

        if self.args.version:
            print(self.VERSION)
            sys.exit(0)


    def init_communication(self):

        # If the serial port is open, close it
        with self.lock:
            if self.ser.isOpen():
                self.ser.close()

        # Setup serial device using selected serial port
        grid.setup_serial(self.ser, self.serial_port, self.lock)

        # Open serial device
        grid.open_serial(self.ser, self.lock)

        # Initialize the Grid+ V2 device
        if grid.initialize_grid(self.ser, self.lock):
            # Set the initial fan speeds based on UI values
            self.initialize_fans()

        else:
            helper.show_error('Could not initialize Grid')

    def initialize_fans(self):
        """Initialize fans to the initial slider values."""

        for i in range(1,7):
            grid.set_fan(ser=self.ser, fan=i, voltage=grid.calculate_voltage(40), lock=self.lock)

if __name__ == "__main__":
    rackfan = RackFan()
