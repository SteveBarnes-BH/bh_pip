#!/usr/bin/env python3
#encoding:utf-8
"""
  Author:  Steve Barnes --<Steven.Barnes@bhge.com>
  Purpose: Find & optionally set a proxy
  Created: 28/08/2019

  The idea of this script is to try various proxy settings to
  locate the one that currently works and optionally set it as
  the default proxy for pip.
"""
from __future__ import print_function
import sys
import os
import re
import subprocess
import winreg
import urllib.request


_COPYRIGHT = """
    BHGE Confidential
    [Unpublished] Copyright 2019.  Baker Hughes, a GE company, LLC.

    NOTICE:  All information contained herein is, and remains the property of
    Baker Hughes, a GE company, LLC, its suppliers, and affiliates, if any.
    The intellectual and technical concepts contained herein are proprietary to
    Baker Hughes, a GE company, LLC and its suppliers and affiliates and may be
    covered by U.S. and Foreign Patents, patents in process, and are protected
    by trade secret and copyright law.
    Dissemination of this information or reproduction of this material is
    strictly forbidden unless prior written permission is obtained from
    Baker Hughes, a GE company, LLC.
"""

ENVSTR = 'https_proxy'

def get_pac_url_from_ie():
    """ Get the list of possible proxies from the IE settings."""
    auto_config_url = None
    print("Checking for AutoConfigURL")
    a_reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    a_key = winreg.OpenKey(
        a_reg,
        r"Software\Microsoft\Windows\CurrentVersion\Internet Settings")
    _, valuecount, _ = winreg.QueryInfoKey(a_key)
    for i in range(valuecount):
        try:
            name, val, _ = winreg.EnumValue(a_key, i)
            if name == "AutoConfigURL":
                auto_config_url = val
        except EnvironmentError:
            pass
    return auto_config_url


def get_proxies_from_ie():
    """ Get the list of possible proxies from the IE settings."""
    proxy_re = re.compile(r'"PROXY\s+(.+:\d+).*"')
    proxy_list = []
    url = get_pac_url_from_ie()
    if url is None:
        return proxy_list
    print(f"Getting Proxies from {url}")
    pac = ""
    try:
        with urllib.request.urlopen(url) as pack:
            pac = pack.read().decode('utf-8')
    except urllib.request.URLError:
        print(f"Failed to read from {url}")
    proxy_list = proxy_re.findall(pac)
    return proxy_list

def getenv(no_env=False):
    """ Get a copy of the environement optionally removing ENVSTR. """
    myenv = os.environ.copy()
    todel = []
    if no_env:
        for key in myenv.keys():
            if ENVSTR.lower() == key.lower():
                todel.append(key)
    for key in todel:
        del myenv[key]
    return myenv

def test_a_proxy(proxy, no_env=False):
    """ Test a single proxy."""
    result = -9
    myenv = getenv(no_env)

    print(f' - Trying pip with --proxy={proxy}', end=' ', flush=True)
    commands = [sys.executable, '-mpip', 'search', 'pip',
                '--retries=2', f"--proxy={proxy}"]
    try:
        result = subprocess.check_call(
            commands, env=myenv,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=10.0,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        print('Fails!')
    else:
        if result == 0:
            print("Works!")
    return result == 0

def test_proxies(no_env=False):
    """ Test the proxies and return those that work. """
    working = []
    proxy_list = ["", ]
    proxy_list.extend(get_proxies_from_ie())
    print(f"Trying {len(proxy_list)} possible proxies!")
    working = [proxy for proxy in proxy_list if test_a_proxy(
        proxy, no_env)]
    return working

def main():
    """ The main function to find a working proxy and use it."""
    envprox = os.getenv(ENVSTR)
    set_no_env = False
    if envprox:
        print(f"Testing HTTPS_PROXY from envionment:\n   ",
              end=' ', flush=True)
        if test_a_proxy(envprox):
            working = [envprox]
        else:
            working = test_proxies()
            if not working:
                print(f"Trying as if SET {ENVSTR.upper()}=",
                      flush=True)
                working = test_proxies(True)
                if working:
                    set_no_env = True
                    print("Now works wuggest using:")
                    print(f"    SET {ENVSTR.upper()}= ",
                          flush=True)
    else:
        working = test_proxies()

    if working:
        errcode = 0 # OK!
    else:
        errcode = "No Working Proxies Found"

    if len(sys.argv) > 2 and working:
        myenv = getenv(set_no_env)
        proxy = working[0]
        print(f"Using: --proxy={proxy}", flush=True)
        commands = [sys.executable, '-mpip']
        commands.extend(sys.argv[1:])
        commands.append(f"--proxy={proxy}")
        errcode = subprocess.call(commands, env=myenv)

    if working:
        print("\nWorking Proxies:")
        print('\n'.join(working))
        if set_no_env:
            print(f"\n\nSuggest Clearing {ENVSTR} with:")
            print(f"    SET {ENVSTR.upper()}= ")
        print("N.B. It may be worth setting your pip default with:")
        proxy = working[0]
        if proxy:
            print(f"\tpip config set global.proxy {proxy}")
        else:
            print(f"\tpip config unset global.proxy")

    sys.exit(errcode)

if __name__ == '__main__':
    main()

