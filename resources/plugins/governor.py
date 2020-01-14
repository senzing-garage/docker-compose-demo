#! /usr/bin/env python3

import logging
import time


class Governor:

    def __init__(self, g2_engine=None):
        self.g2_engine = g2_engine

        log_format = '%(asctime)s %(message)s'
        logging.basicConfig(format=log_format, level=logging.INFO)

    def govern(self):
        sleep_time = 15
        logging.info("Governor is sleeping {0}".format(sleep_time))
        time.sleep(sleep_time)


if __name__ == '__main__':
    pass
