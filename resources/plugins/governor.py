#! /usr/bin/env python3

import logging
import time


class Governor:

    def __init__(self, g2_engine=None):

        # Store parameters in instance variables.

        self.g2_engine = g2_engine

        # Configure logging.

        log_format = '%(asctime)s %(message)s'
        logging.basicConfig(format=log_format, level=logging.INFO)

        # Instance variables.

        self.counter = 0
        self.stride = 500

    def govern(self):
        """
        Do the actual "governing".
        Do not return until the governance has been completed.
        The caller of govern() waits synchronously.
        """

        # Faux governance.  Replace with actual governance.

        self.counter += 1

        if self.counter % self.stride == 0:
            sleep_time = 15
            logging.info("Sample Governor is sleeping {0} seconds for record {1}.  Replace the Governor class with your code.".format(sleep_time, self.counter))
            time.sleep(sleep_time)


if __name__ == '__main__':
    pass
