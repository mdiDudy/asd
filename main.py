import psutil

def get_cpu_info():
    cpu_info = {
        "Physical cores": psutil.cpu_count(logical=False),
        "Total cores": psutil.cpu_count(logical=True),
        "Max Frequency": f"{psutil.cpu_freq().max:.2f}Mhz",
        "Min Frequency": f"{psutil.cpu_freq().min:.2f}Mhz",
        "Current Frequency": f"{psutil.cpu_freq().current:.2f}Mhz",
        "CPU Usage Per Core": [f"{x}%" for x in psutil.cpu_percent(percpu=True, interval=1)],
        "Total CPU Usage": f"{psutil.cpu_percent(interval=1)}%"
    }
    return cpu_info

def get_memory_info():
    svmem = psutil.virtual_memory()
    memory_info = {
        "Total": f"{svmem.total / (1024 ** 3):.2f} GB",
        "Available": f"{svmem.available / (1024 ** 3):.2f} GB",
        "Used": f"{svmem.used / (1024 ** 3):.2f} GB",
        "Percentage": f"{svmem.percent}%"
    }
    return memory_info

def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info.append({
            "Device": partition.device,
            "Mountpoint": partition.mountpoint,
            "File system type": partition.fstype,
            "Total Size": f"{usage.total / (1024 ** 3):.2f} GB",
            "Used": f"{usage.used / (1024 ** 3):.2f} GB",
            "Free": f"{usage.free / (1024 ** 3):.2f} GB",
            "Percentage": f"{usage.percent}%"
        })
    return disk_info

if __name__ == "__main__":
    print("CPU Info:")
    for k, v in get_cpu_info().items():
        print(f"{k}: {v}")
    
    print("\nMemory Info:")
    for k, v in get_memory_info().items():
        print(f"{k}: {v}")
    
    print("\nDisk Info:")
    for disk in get_disk_info():
        for k, v in disk.items():
            print(f"{k}: {v}")
        print()
