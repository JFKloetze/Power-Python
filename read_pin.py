import sys
from IOPi import IOPi

pin = sys.argv[2]
port  = int((pin-1)/8)

bus = IOPi(sys.argv[1])
bus.set_port_direction(port, 0x01)

print bus.read(pin)

