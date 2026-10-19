from Device import Device
from threading import Thread
from time import sleep

class Location(Thread):
    def __init__(self, location_name: str):
        super().__init__()
        self._location_name = location_name
        self._devices = []
        self._location_status = "INIT"
        self._device_count = 0
        self._current_device = 0

    def __repr__(self):
        return f"{self._location_name}: {repr(self._devices[self._current_device])}"

    def getLocationName(self:Location) -> str:
        return self._location_name

    def run(self):
        #print(f"Starting Thread for {self._location_name} - {self.name}")
        while self._current_device != self._device_count:
            #print(f"Starting {self._location_name} - {self._devices[self._current_device]}")
            self._devices[self._current_device].start()
            while True:
                if(self._devices[self._current_device].is_alive()):
                    sleep(1)
                else:
                    break
            self._current_device += 1

        pass

    def addDevice(self, device_name: str, device_ip: str):
        self._devices.append(Device(device_name, device_ip))
        self._device_count += 1
        #   print(f"{self._location_name} - {self._devices}")

    def loadDevices(self):
        pass