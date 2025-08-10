import json
from typing import Dict

from .message import Messenger

def process_trigger_data(data: Dict):
    if data.get("f") != "t":
        return
    time_stamp = data["t"]
    status = data["s"]
    # print(f"[Trigger] time={time_stamp}, status={status}")


def process_imu_data(data: Dict):
    if data.get("f") != "imu":
        return
    imu = {
        "time_stamp_us": data["t"],
        "a": data["d"][:3],
        "g": data["d"][3:6],
        "temperature": data["d"][6],
        "q": data["q"][:4]
    }
    Messenger.get_instance().pub("imu_1", json.dumps(imu))


def process_gps_data(data: Dict):
    if data.get("f") != "GNGGA":
        return
    gps = {
        "data": data["d"],
        "trigger_time_us": data["pps"],
        "time_stamp_us": data["t"]
    }
    Messenger.pub("gps", json.dumps(gps))

def process_log_data(data: Dict):
    if data.get("f") != "log":
        return
    level = data.get("l", "INFO")
    msg = data.get("msg", "")
    print(f"[LOG-{level}] {msg}")
