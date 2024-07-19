import os
import psutil

def check_system_info():
    # Check number of CPU cores
    cpu_cores = os.cpu_count()
    print(f"Number of CPU cores: {cpu_cores}")

    # Check amount of RAM
    ram_info = psutil.virtual_memory()
    total_ram = ram_info.total / (1024 ** 3)  # Convert bytes to GB
    print(f"Total RAM: {total_ram:.2f} GB")

if __name__ == "__main__":
    check_system_info()
