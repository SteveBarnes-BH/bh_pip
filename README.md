# ge_pip
A pip wrapper that does its best to cope with the proxy settings

Author: Steve Barnes (212303160) Steven.Barnes@BakerHughes.com 

## Licence: 
This code is free to use for all within the GE and Related Companies.
This code is supplied without any warranty and any support is given on an ad-hock basis.

This code should work with python 2.7 and >3.5

## Usage
This code can be used either as simply:

    python ge_pip.py

Where it will try to establish a working set of settings for pip and recommend them to you OR

    python ge_pip.py pip_comnads...

Where it will do the above then use the recommended settings to run the command(s). This is
useful when you don't wish to change your settings but need a one off run of pip but it is 
not working in the current situation.
