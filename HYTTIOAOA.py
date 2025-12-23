#!/usr/bin/env python3

import subprocess
import time
import platform
import sys

def getPlatformCommands(state):
    currentOS = platform.system()
    
    if currentOS == "Linux":
        if subprocess.run(["which", "nmcli"], stdout=subprocess.DEVNULL).returncode == 0:
            return ["nmcli", "radio", "wifi", state]
        return ["rfkill", "unblock" if state == "on" else "block", "wifi"]

    if currentOS == "Darwin":
        return ["networksetup", "-setairportpower", "en0", state]

    if currentOS == "Windows":
        winState = "ENABLED" if state == "on" else "DISABLED"
        return ["netsh", "interface", "set", "interface", "Wi-Fi", f"admin={winState}"]

    raise OSError(f"Unsupported OS: {currentOS}")

def setWifiState(state):
    try:
        cmd = getPlatformCommands(state)
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def HYTTIOAOA(duration=15):
    print(f"OS: {platform.system()}")
    print(f"Toggling wifi for {duration}s...")
    setWifiState("off")
    time.sleep(duration)
    setWifiState("on")
    print("Done.")

if __name__ == "__main__":
    waitTime = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    HYTTIOAOA(waitTime)
