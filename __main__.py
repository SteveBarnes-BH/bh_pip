#!usr/bin python3
import sys
if sys.version_info.major > 2:
    import ge_pip
else:
    import ge_pip_py2 as ge_pip

ge_pip.main()
