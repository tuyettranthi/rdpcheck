import subprocess

def join_vps_rdp(ip_address, username, password):
    cmd = f"xfreerdp /u:{username} /p:{password} /v:{ip_address}"
    process = subprocess.Popen(cmd, shell=True)
    process.wait()

def change_vps_rdp_password(ip_address, username, old_password, new_password):
    # Run command to change password using net user command
    cmd = f"net user {username} {new_password}"
    process = subprocess.Popen(f"xfreerdp /u:{username} /p:{old_password} /v:{ip_address} /cert-ignore && {cmd}", shell=True)
    process.wait()

# Usage example
ip_address = "18.195.148.47"
username = "root"
password = "1"
new_password = "adomanbg@123"

join_vps_rdp(ip_address, username, password)
change_vps_rdp_password(ip_address, username, password, new_password)
