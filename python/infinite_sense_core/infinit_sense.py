import threading
import time
import logging

class Synchronizer:
    def __init__(self):
        self.net_manager = None
        self.serial_manager = None
        self.sensor_manager = None
        self.net_ip = None
        self.net_port = None
        self.serial_dev = None
        self.serial_baud_rate = None
        self._lock = threading.Lock()

        logging.info("\n"
                     "  ▗▄▄▄▖▗▖  ▗▖▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖ ▗▄▄▖▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖▗▄▄▄▖\n"
                     "    █  ▐▛▚▖▐▌▐▌     █  ▐▛▚▖▐▌  █    █  ▐▌   ▐▌   ▐▌   ▐▛▚▖▐▌▐▌   ▐▌   \n"
                     "    █  ▐▌ ▝▜▌▐▛▀▀▘  █  ▐▌ ▝▜▌  █    █  ▐▛▀▀▘ ▝▀▚▖▐▛▀▀▘▐▌ ▝▜▌ ▝▀▚▖▐▛▀▀▘\n"
                     "  ▗▄█▄▖▐▌  ▐▌▐▌   ▗▄█▄▖▐▌  ▐▌▗▄█▄▖  █  ▐▙▄▄▖▗▄▄▞▘▐▙▄▄▖▐▌  ▐▌▗▄▄▞▘▐▙▄▄▖")

    def set_log_path(self, path):
        logging.basicConfig(filename=path, level=logging.INFO,
                            format='[%(asctime)s] %(levelname)s: %(message)s')

    def set_net_link(self, net_ip, net_port):
        self.net_ip = net_ip
        self.net_port = net_port
        from infinite_sense_core.net import NetManager
        self.net_manager = NetManager(net_ip, net_port)

    def set_usb_link(self, serial_dev, serial_baud_rate):
        self.serial_dev = serial_dev
        self.serial_baud_rate = serial_baud_rate
        from usb import UsbManager
        self.serial_manager = UsbManager(serial_dev, serial_baud_rate)
        self.net_manager = None

    def use_sensor(self, sensor):
        self.sensor_manager = sensor

    def start(self):
        with self._lock:
            try:
                if self.net_manager:
                    self.net_manager.start()
                if self.serial_manager:
                    self.serial_manager.start()
                if self.sensor_manager:
                    time.sleep(2)
                    self.sensor_manager.initialization()
                    self.sensor_manager.start()
                logging.info("Synchronizer Started.")
            except Exception as e:
                logging.error(f"Synchronizer start exception: {e}")

    def stop(self):
        with self._lock:
            try:
                if self.net_manager:
                    self.net_manager.stop()
                if self.serial_manager:
                    self.serial_manager.stop()
                if self.sensor_manager:
                    self.sensor_manager.stop()
                logging.info("Synchronizer Stopped.")
            except Exception as e:
                logging.error(f"Synchronizer stop exception: {e}")
