import argparse
import threading
import serial
from rackfan import grid
import sys
import time

class RackFan:
    def __init__(self, args) -> None:
        self.args = args

    def init_communication(self):
         # Serial communication object
        self.ser = serial.Serial()


        # Object for locking the serial port while sending/receiving data
        self.lock = threading.Lock()

        # Use the specified serial port or default to the first available one
        serial_ports = grid.get_serial_ports()
        self.serial_port = self.args.serial or serial_ports[0]


        # If the serial port is open, close it
        with self.lock:
            if self.ser.isOpen():
                self.ser.close()

        # Setup serial device using selected serial port
        grid.setup_serial(self.ser, self.serial_port, self.lock)

        # Open serial device
        grid.open_serial(self.ser, self.lock)

        # Initialize the Grid+ V2 device
        grid.initialize_grid(self.ser, self.lock)

    def get_speeds(self):
        return grid.read_fan_rpm(ser=self.ser, lock=self.lock)

    def initialize_fans(self):
        """Initialize fans to the initial slider values."""

        for i in range(1,7):
            grid.set_fan(ser=self.ser, fan=i, voltage=grid.calculate_voltage(40), lock=self.lock)

    def set_fan(self, fan_number:int, fan_speed:int):
        grid.set_fan(ser=self.ser, fan=fan_number, voltage=grid.calculate_voltage(fan_speed), lock=self.lock)
        time.sleep(1)
        print(grid.read_fan_rpm(ser=self.ser,lock=self.lock))
       

def main():

    parser = argparse.ArgumentParser(description='Control fans connected to NZXT GRID+ V2')
    parser.add_argument("-s", "--serial", help="specify the serial port to use")
    parser.add_argument("-f", "--fan", action='append', help="specify a fan number to control (used with -o)", type=int)
    parser.add_argument("-p", "--percentage", help='set fan speed to x percent (used with -o)', type=int)

    args = parser.parse_args()
    rackfan = RackFan(args)
    
    rackfan.init_communication()

    for current_fan in args.fan:
        rackfan.set_fan(current_fan, args.percentage)

if __name__ == "__main__":
    main()
