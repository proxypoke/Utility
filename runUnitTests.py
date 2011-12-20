#!/usr/bin/python2

# This program is Free Software under the terms of
# the Do What The Fuck You Want To Public License (WTFPL)
# See wtfpl.txt or http://sam.zoy.org/wtfpl/COPYING
# for a copy of the license.

# Revursively discover and run unittest suites in a directory
# and its subdirectories.

# You can pass a number as an argument for the script to change
# verbosity. Default is 2.

import unittest
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            vlevel = int(sys.argv[1])
            print("Verbosity set to {0}.".format(vlevel))
        else:
            print("Argument not recognized. You need to specify a "
                    "positive integer.")
            exit(1)
    else:
        print("No verbosity specified. Assuming default (2).")
        vlevel = 2


    loader = unittest.TestLoader()

    suite = loader.discover(".", "*.py")

    ttr = unittest.TextTestRunner(verbosity=vlevel)

    ttr.run(suite)
