from nike_devices import NikeCiscoDevice
from pprint import pprint


device = NikeCiscoDevice("192.168.178.1", "jenkins", "jenkins")
pprint(device.get_interface_brief())
