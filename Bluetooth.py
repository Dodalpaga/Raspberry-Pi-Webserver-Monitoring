#!/usr/bin/python3
 
import dbus
from subprocess import check_output
 
from advertisement import Advertisement
from service import Application, Service, Characteristic, Descriptor
 
GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
 
class IPAddressAdvertisement(Advertisement):
    def __init__(self, index):
        Advertisement.__init__(self, index, "peripheral")
        self.include_tx_power = True
 
class IPAddressService(Service):
    IPADDR_SVC_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
 
    def __init__(self, index):
        Service.__init__(self, index, self.IPADDR_SVC_UUID, True)
        self.add_characteristic(IPAddressCharacteristic(self))
 
class IPAddressCharacteristic(Characteristic):
    IPADDR_CHARACTERISTIC_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
 
    def __init__(self, service):
        Characteristic.__init__(
                self, self.IPADDR_CHARACTERISTIC_UUID,
                ["read"], service)
 
    def ReadValue(self, options):
        value = []
 
        ipaddrs = check_output(["ObCP", "-I"])
        ipaddr = ipaddrs.split()[0]
        for c in ipaddr:
            value.append(dbus.Byte(c))
 
        return value
 
app = Application()
app.add_service(IPAddressService(0))
app.register()
 
adv = IPAddressAdvertisement(0)
adv.register()
 
try:
    app.run()
except KeyboardInterrupt:
    app.quit()
    print("\nGATT application terminated")