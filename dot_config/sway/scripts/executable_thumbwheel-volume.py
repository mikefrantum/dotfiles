#!/usr/bin/env python3
import evdev
import subprocess

DEVICE = "/dev/input/event6"
REL_HWHEEL = 6

device = evdev.InputDevice(DEVICE)

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_REL and event.code == REL_HWHEEL:
        if event.value > 0:
            subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "-5%"])
        elif event.value < 0:
            subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "+5%"])
