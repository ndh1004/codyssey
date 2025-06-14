import multiprocessing
import threading
import platform
import random
import psutil
import json
import time

class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 2)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 2)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 2)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500, 715), 2)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 4)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 2)

    def get_env(self):
        return self.env_values

class MissionComputer:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None
        }
        self.sensor = DummySensor()

    def get_sensor_data(self):
        while True:
            self.sensor.set_env()
            self.env_values = self.sensor.get_env()
            print(json.dumps(self.env_values, indent=4))
            time.sleep(5)

    def get_mission_computer_info(self):
        try:
            info = {
                "OS": platform.system(),
                "OS VERSION": platform.version(),
                "CPU TYPE": platform.processor(),
                "CPU CORES": psutil.cpu_count(logical=True),
                "TOTAL MEMORY (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2)
            }
            print(" [ MISSION COMPUTER SYSTEM INFO ] ")
            print(json.dumps(info, indent=4, ensure_ascii=False))
        except Exception as e:
            print("Error getting system info")

    def get_mission_computer_load(self):
        try:
            load = {
                "CPU USAGE (%)": psutil.cpu_percent(interval=1),
                "MEMORY USAGE (%)": psutil.virtual_memory().percent
            }
            print(" [ MISSION COMPUTER USAGE INFO ] ")
            print(json.dumps(load, indent=4, ensure_ascii=False))
        except Exception as e:
            print("Error getting system load info")


def run_info():
    runComputer = MissionComputer()
    while True:
        runComputer.get_mission_computer_info()
        time.sleep(20)

def run_load():
    runComputer = MissionComputer()
    while True:
        runComputer.get_mission_computer_load()
        time.sleep(20)

def run_sensor():
    runComputer = MissionComputer()
    runComputer.get_sensor_data()
    
if __name__ == "__main__":
    
    p1 = multiprocessing.Process(target=run_info)
    p2 = multiprocessing.Process(target=run_load)
    p3 = multiprocessing.Process(target=run_sensor)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()