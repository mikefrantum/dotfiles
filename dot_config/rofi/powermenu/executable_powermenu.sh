#!/usr/bin/env bash

# Options
shutdown="⏻  Shutdown"
reboot="  Reboot"
suspend="  Suspend"
logout="  Logout"
lock="  Lock"

# Rofi command
rofi_cmd() {
    rofi -dmenu \
        -p "Power" \
        -theme "~/.config/rofi/themes/powermenu.rasi"
}

chosen=$(printf '%s\n' "$lock" "$suspend" "$logout" "$reboot" "$shutdown" | rofi_cmd)

case $chosen in
    "$shutdown")
        systemctl poweroff ;;
    "$reboot")
        systemctl reboot ;;
    "$suspend")
        systemctl suspend ;;
    "$logout")
        swaymsg exit ;;
    "$lock")
        swaylock ;;
esac
