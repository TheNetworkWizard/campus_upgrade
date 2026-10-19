from Location import Location
from time import sleep

device_list = {
    "QE01": {
        'Switch 1': "1.1.1.1",
        "Switch 2": "2.2.2.2",
        "Switch 3": "3.3.3.3"
    },
    "QE02": {
        "Switch 11": "2.1.1.1",
        "Switch 22": "2.1.1.2",
        "Switch 33": "2.1.1.3"
    },
    "QE03": {
        "Switch 11": "2.1.1.1",
        "Switch 22": "2.1.1.2",
        "Switch 33": "2.1.1.3"
    },
    "QE04": {
        "Switch 11": "2.1.1.1",
        "Switch 22": "2.1.1.2",
        "Switch 33": "2.1.1.3"
    }
}

locations = []

if __name__ == "__main__":
    for location, devices in device_list.items():
        locations.append(Location(location_name=location))
        for device_name, device_ip in devices.items():
            #print(f"Adding {device_name} to {location}")
            locations[-1].addDevice(device_name, device_ip)
        locations[-1].start()
        

    #for location in locations:
    #    location.start()
    
    while True:
        completed_locations = 0
        for location in locations:
            if(location.is_alive()):
                print(f"{str(location):<50}")
            else:
                print(f"{str(location.getLocationName() + " - Completed"):<50}")
                completed_locations += 1
                if completed_locations == len(locations):
                    exit()
        print(f"\033[{len(locations)}A", end="")
        sleep(1)
    