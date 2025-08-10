import logging
import time
from infinite_sense_core.infinit_sense import Synchronizer
from infinite_sense_core.message import Messenger


class MockSensor:
    def initialization(self):
        logging.info("MockSensor initialized")

    def start(self):
        logging.info("MockSensor started")

    def stop(self):
        logging.info("MockSensor stopped")

def imu_callback(msg_bytes, size):
    logging.info(f"Received IMU data of size {size}")

def image_callback(msg_bytes, size):
    logging.info(f"Received image data of size {size}")

def main():
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] %(levelname)s: %(message)s',
                        handlers=[
                            logging.FileHandler("synchronizer.log", mode='a', encoding='utf-8'),
                            logging.StreamHandler()
                        ])

    synchronizer = Synchronizer()

    synchronizer.set_log_path("synchronizer.log")

    synchronizer.set_net_link("192.168.1.188", 8888)

    sensor = MockSensor()
    synchronizer.use_sensor(sensor)

    synchronizer.start()

    messenger = Messenger.get_instance()
    messenger.sub("imu_1", imu_callback)
    messenger.sub("cam_1", image_callback)

    logging.info("Synchronizer is running. Press Ctrl+C to exit.")

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        logging.info("Stopping synchronizer due to keyboard interrupt...")

    synchronizer.stop()

if __name__ == "__main__":
    main()
