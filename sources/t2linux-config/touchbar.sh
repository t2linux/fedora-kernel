#!/usr/bin/env bash
set -euo pipefail
echo "Select Touch Bar mode"
echo
echo "0: Only show F1-F12"
echo "1: Show media and brightness controls, use the fn key to switch to F1-F12"
echo "2: Show F1-F12, use the fn key to switch to media and brightness controls"
echo "3: Only show media and brightness controls"
echo "4: Only show the escape key"
read tb
if [[ \$tb != 0 && \$tb != 1 && \$tb != 2 && \$tb != 3 && \$tb != 4 ]]
then
echo "Invalid input. Aborting!"
exit 1
fi
echo "Changing default mode ..."
echo "# display f* key in touchbar" > /etc/modprobe.d/apple-tb.conf
echo "options apple-touchbar fnmode=\$tb" >> /etc/modprobe.d/apple-tb.conf
bash -c "echo \$tb > /sys/class/input/*/device/fnmode"
echo "Done!"
