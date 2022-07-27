from nike_devices import NikeCiscoDevice
from pprint import pprint


device = NikeCiscoDevice("192.168.178.1", "admin", "!mlh1985")
pprint(device.get_interface_brief('genie))
