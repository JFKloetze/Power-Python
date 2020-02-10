import sys
from IOPi import IOPi

anzahl_pins = (len(sys.argv)-2)/2

pins = int(sys.argv[2:(2+anzahl_pins)])
werte = int(sys.argv[(2+anzahl_pins):(2+2*anzahl_pins+1)])

port  = int((pins[0]-1)/8)

bus = IOPi(sys.argv[1])
bus.set_port_direction(port, 0x00)

for i in range(1,anzahl_pins+1):
	bus.write(pins[i],werte[i])


