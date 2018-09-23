#!/usr/bin/env python
# MAC Changer
# by Dante

# Using a module to execute system commands
import subprocess
import optparse

def get_arguments():
    """

    """
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address.")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address.")

    if not options.Interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")

    return parser.parse_args()

def change_mac(interface, mac):
    """

    """
    print("[+] Changing MAC address for " + interface + " to " + mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_arguments()
change_mac(options.interface, options.mac)
