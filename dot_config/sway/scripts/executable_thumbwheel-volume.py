#!/usr/bin/env python3
import evdev
import subprocess

DEVICE_NAME = "MX Master"
REL_HWHEEL = 6

def find_device(name):
    for path in evdev.list_devices():
        dev = evdev.InputDevice(path)
        if name in dev.name and evdev.ecodes.EV_REL in dev.capabilities():
            return dev
    return None

device = find_device(DEVICE_NAME)
if device is None:
    raise SystemExit(f"Device '{DEVICE_NAME}' not found")

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_REL and event.code == REL_HWHEEL:
        if event.value > 0:
            subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "-5%"])
        elif event.value < 0:
            subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "+5%"])
