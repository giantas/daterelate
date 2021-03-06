#! /usr/bin/env python3

import os
import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(
        os.path.abspath(__file__)
    )
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)
