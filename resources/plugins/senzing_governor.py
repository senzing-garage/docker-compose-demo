#! /usr/bin/env python3

import logging
import time


class Governor:

    def __init__(self, g2_engine=None, hint=None):

        # Store parameters in instance variables.

        self.g2_engine = g2_engine
        self.hint = hint

        # Configure logging.

        log_format = '%(asctime)s %(message)s'
        logging.basicConfig(format=log_format, level=logging.INFO)

        # Instance variables.

        self.counter = 0
        self.stride = 500
        self.sleep_time = 15

    def govern(self):
        """
        Do the actual "governing".
        Do not return until the governance has been completed.
        The caller of govern() waits synchronously.
        """

        # Faux governance.  Replace with actual governance.

        self.counter += 1

        if self.counter % self.stride == 0:
            logging.info("Sample Governor is sleeping {0} seconds on record {1}. Hint: {2}. Replace the Governor class with your code.".format(self.sleep_time, self.counter, self.hint))
            time.sleep(self.sleep_time)


if __name__ == '__main__':
    pass
