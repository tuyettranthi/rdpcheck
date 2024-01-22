import subprocess

command = 'qemu-system-x86_64 -m 9G -cpu core2duo -boot order=c -drive file=win.iso,media=cdrom -drive file=win.img,format=raw -device usb-ehci,id=usb,bus=pci.0,addr=0x4 -device usb-tablet -vnc :0 -smp cores=24,threads=8 -device e1000,netdev=n0 -netdev user,id=n0 -vga vmware'

process = subprocess.Popen(command, shell=True)
