#!/bin/bash

# Update system
sudo apt update -y

# Download win.iso
wget -O win.iso "https://go.microsoft.com/fwlink/p/?LinkID=2195443&clcid=0x409&culture=en-us&country=US97343242&h=6969ba065476fa37696095af393a826397c50b3a373cab922e332816d6d4a849"

# Download ngrok.tgz
wget -O ngrok.tgz "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz"

# Extract ngrok.tgz
tar -xf ngrok.tgz

# Remove ngrok.tgz
rm -rf ngrok.tgz

# Configure ngrok
./ngrok config add-authtoken 2TT1L7pPryMzmZ4zFhxna8uR7Ds_ygTuwXssJ2R2utoFb8NE

# Install qemu-kvm
sudo apt install qemu-kvm -y

# Create qemu image
qemu-img create -f raw win.img 512G

# Run qemu virtual machine
qemu-system-x86_64 -m 9G -cpu core2duo -boot order=c -drive file=win.iso,media=cdrom -drive file=win.img,format=raw -device usb-ehci,id=usb,bus=pci.0,addr=0x4 -device usb-tablet -vnc :0 -smp cores=24,threads=8 -device e1000,netdev=n0 -netdev user,id=n0 -vga vmware
