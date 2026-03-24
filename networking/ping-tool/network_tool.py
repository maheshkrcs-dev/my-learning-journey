import os
import platform

def ping_host(host):
    print(f"\nPinging {host}...\n")
    
    # Windows vs Linux/Mac
    param = "-n 4" if platform.system().lower() == "windows" else "-c 4"
    
    command = f"ping {param} {host}"
    
    result = os.system(command)
    
    if result == 0:
        print("\n✅ Host is reachable\n")
    else:
        print("\n❌ Host is NOT reachable\n")

# Main program
if __name__ == "__main__":
    host = input("Enter website or IP: ")
    ping_host(host)
