import subprocess

def check_connection(host):
    # This uses the system's 'ping' to check connectivity
    # It works for both IPv4 and IPv6!
    try:
        # -c 1 means 1 packet, -W 2 means wait 2 seconds
        subprocess.check_output(["ping", "-c", "1", "-W", "2", host])
        return True
    except subprocess.CalledProcessError:
        return False

sites = ["google.com", "github.com", "8.8.8.8"]

print("--- Network Status Report ---")
for s in sites:
    status = "ALIVE ✅" if check_connection(s) else "DEAD ❌"
    print(f"{s}: {status}")
