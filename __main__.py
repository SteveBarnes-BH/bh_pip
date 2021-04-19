#!python3
from __future__ import print_function

"""
This is the top level of ge_pip - all it does is to select between the 
python 2 & 3 versions of the code based on the python version that it is
invoked from.
"""
_COPYRIGHT = """
    Baker Hughes Confidential
    [Unpublished] Copyright 2021.  Baker Hughes LLC.

    NOTICE:  All information contained herein is, and remains the property of
    Baker Hughes LLC, its suppliers, and affiliates, if any.
    The intellectual and technical concepts contained herein are proprietary to
    Baker Hughes LLC and its suppliers and affiliates and may be
    covered by U.S. and Foreign Patents, patents in process, and are protected
    by trade secret and copyright law.
    Dissemination of this information or reproduction of this material is
    strictly forbidden unless prior written permission is obtained from
    Baker Hughes LLC.
"""

import sys

# Import the appropriate version of the code.
if sys.version_info.major > 2:
    import bh_pip
else:
    import bh_pip_py2 as bh_pip
from defaults import DESCRIPTION

if __name__ == "__main__":
    if "--help" in sys.argv:
        print(DESCRIPTION)
    else:
        print("Checking possible pip proxies for python", sys.version)
        bh_pip.main(True)
