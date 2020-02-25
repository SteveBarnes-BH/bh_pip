#!/usr/bin/env python3
# encoding:utf-8
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
import urllib.request

if sys.platform == "win32":
    import winreg


_COPYRIGHT = """
    Baker Hughes Confidential
    [Unpublished] Copyright 2019-2020.  Baker Hughes LLC.

    NOTICE:  All information contained herein is, and remains the property of
    Baker Hughes, a GE company, LLC, its suppliers, and affiliates, if any.
    The intellectual and technical concepts contained herein are proprietary to
    Baker Hughes LLC and its suppliers and affiliates and may be
    covered by U.S. and Foreign Patents, patents in process, and are protected
    by trade secret and copyright law.
    Dissemination of this information or reproduction of this material is
    strictly forbidden unless prior written permission is obtained from
    Baker Hughes LLC.
"""

ENVSTR = "https_proxy"
ENVSTR2 = "http_proxy"
DEFAULT_PAC_URL = "https://cloudproxy.setpac.ge.com/pac.pac"

if sys.platform == "win32":
    # The following will only work on Windows platforms
    def get_pac_url_from_ie():
        """ Get the list of possible proxies from the IE settings."""
        auto_config_url = DEFAULT_PAC_URL
        print("Checking for AutoConfigURL")
        a_reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        a_key = winreg.OpenKey(
            a_reg, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        )
        _, valuecount, _ = winreg.QueryInfoKey(a_key)
        for i in range(valuecount):
            try:
                name, val, _ = winreg.EnumValue(a_key, i)
                if name == "AutoConfigURL":
                    auto_config_url = val
            except EnvironmentError:
                pass
        print("Auto Config URL", auto_config_url)
        return auto_config_url


else:
    # Non-Windows alternative
    def get_pac_url_from_ie():
        """ On non windows platforms this isn't an option so use fixed """
        return DEFAULT_PAC_URL


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
        with urllib.request.urlopen(url, timeout=3) as pack:
            pac = pack.read().decode("utf-8")
    except urllib.request.URLError:
        print(f"Failed to read from {url}")
    proxy_list = proxy_re.findall(pac)
    for proxy in proxy_list:
        if not proxy.lower().startswith("http"):
            proxy_list.append("http://" + proxy)
    return proxy_list


def getenv(no_env=False):
    """ Get a copy of the environment optionally removing ENVSTR. """
    myenv = os.environ.copy()
    removes = [ENVSTR.lower(), ENVSTR2.lower()]
    todel = []
    if no_env:
        for key in myenv.keys():
            if key.lower() in removes:
                todel.append(key)
    for key in todel:
        del myenv[key]
    return myenv


def test_a_proxy(proxy, no_env=False):
    """ Test a single proxy."""
    result = "Not Tested"
    myenv = getenv(no_env)

    print(f" - Trying pip with --proxy={proxy}", end=" ", flush=True)
    commands = [
        sys.executable,
        "-mpip",
        "search",
        "pip",
        "--retries=2",
        f"--proxy={proxy}",
    ]
    try:
        result = subprocess.check_call(
            commands,
            env=myenv,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=10.0,
        )
    except subprocess.CalledProcessError:
        result = "[Error]"
    except subprocess.TimeoutExpired:
        result = "[Timeout]"

    if result == 0:
        print("Works!")
    else:
        print("Fails! Returned:", result)
    sys.stdout.flush()
    return result == 0


def test_proxies(no_env=False):
    """ Test the proxies and return those that work. """
    working = []
    proxy_list = [
        "",
    ]  # Start with no command line proxy
    proxy_list.extend(get_proxies_from_ie())
    if no_env:
        print(
            "Trying as if:\n\tSET %s=\n\tSET %s=\nhad been done!"
            % (ENVSTR.upper(), ENVSTR2.upper()),
            flush=True,
        )
    print(f"Trying {len(proxy_list)} possible proxies!")
    working = [proxy for proxy in proxy_list if test_a_proxy(proxy, no_env)]
    if working and no_env:
        print("Now works suggest changing environment proxies", flush=True)
    return working


def report_working(working, set_no_env):
    """ Report which proxies are working."""
    print("\nWorking Proxies:")
    print("\n--proxy=", "\n--proxy=".join(working))
    if set_no_env:
        print("\n\nSuggest Clearing environmental proxies with:")
        for envsetting in [ENVSTR, ENVSTR2]:
            print("    SET %s= " % envsetting.upper())
        print("or equivelent!")
    print("N.B. It may be worth setting your pip default with:")
    proxy = working[0]
    if proxy:
        print(f"\tpip config set global.proxy {proxy}")
    else:
        print(f"\tpip config unset global.proxy")


def main(pause=False):
    """ The main function to find a working proxy and use it."""
    set_no_env = False
    envs_found = False
    working = []
    for envsetting in [ENVSTR, ENVSTR2]:
        envprox = os.getenv(envsetting)
        if envprox:
            envs_found = True
            print("Testing %s from envionment:\n   " % envsetting, end=" ")
            sys.stdout.flush()
            if test_a_proxy(envprox):
                working.append(envprox)

    if not working:  # So try the proxies we can find
        working = test_proxies()

    if not working and envs_found:  # Still no but env settings found
        working = test_proxies(True)
        set_no_env = len(working) > 0

    if working:
        errcode = 0  # OK!
    else:
        errcode = "No Working Proxies Found"

    if len(sys.argv) > 2 and working:
        print("Now trying your command(s)")
        myenv = getenv(set_no_env)
        proxy = working[0]
        print(f"Using: --proxy={proxy}", flush=True)
        sys.stdout.flush()
        commands = [sys.executable, "-mpip"]
        commands.extend(sys.argv[1:])
        commands.append(f"--proxy={proxy}")
        errcode = subprocess.call(commands, env=myenv)

    if working:
        report_working(working, set_no_env)
    else:
        print(errcode)

    if pause:
        dummy = input("Press enter to continue!")
    sys.exit(errcode)


if __name__ == "__main__":
    main()
