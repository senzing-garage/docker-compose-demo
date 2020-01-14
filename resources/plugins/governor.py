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

    def govern(self):
        """
        Do the actual "governing".
        Do not return until the governance has been completed.
        The caller of govern() waits synchronously.
        """

        # Faux governance.  Replace with actual governance.

        sleep_time = 15
        logging.info("Governor is sleeping {0} seconds.  Replace the Governor class with your code".format(sleep_time))
        time.sleep(sleep_time)


if __name__ == '__main__':
    pass
