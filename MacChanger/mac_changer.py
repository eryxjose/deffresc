#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address.")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please, specify an interface. Use --help for more info.")
    elif not options.new_mac:
        parser.error("Please, specify an new_mac. Use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print(f"Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ip", "link", "set", interface, "down"])
    subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac])
    subprocess.call(["ip", "link", "set", interface, "up"])
    subprocess.call(f"/etc/init.d/networking restart", shell=True)

def get_current_mac(interface):
    result_subprocess = str(subprocess.check_output(["ip", "addr", "show", interface]))
    result_re = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result_subprocess)
    if result_re:
        return result_re.group(0)
    else:
        print("Could not found MAC address.")


# get command line arguments and execute change_mac

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC: " + str(current_mac))
#change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("Success.")
else:
    print("Error.")



