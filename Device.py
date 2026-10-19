from time import sleep
from random import randint
from threading import Thread

class Device(Thread):
    def __init__(self, device_name: str, device_ip: str):
        super().__init__()
        self._device_name = device_name
        self._device_ip = device_ip
        self._device_status = "INIT"
        self.daemon = True

    def __repr__(self):
        return f"{self._device_name} - {self._device_status}"

    def run(self):
        #print(f"Starting Thread for {self._device_name} - {self.name}")
        self.connectToDevice()
        self.copySoftware()
        self.installSoftware()

    def connectToDevice(self):
        self._device_status = "Connecting"
        sleep(randint(2,4))

    def copySoftware(self):
        self._device_status = "Copying Software"
        sleep(randint(2,9))

    def installSoftware(self):
        self._device_status = "Installing Software"
        sleep(randint(2,9))