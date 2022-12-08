import datetime
import time
import platform as deviceinfo

device_CPU = deviceinfo.processor()
if device_CPU == "":
    device_CPU = "Unknown processor"

device_OS = deviceinfo.system()
if device_OS == "Windows":
    device_OS = deviceinfo.win32_ver()
elif device_OS == "Darwin":
    deviceOS = deviceinfo.mac_ver()
    if device_OS == "":
        device_OS = "Unknown MacOS version"
elif device_OS == "Linux":
    try:
        device_OS = deviceinfo.freedesktop_os_release()
        device_OS = device_OS["NAME"]
    except:
        device_OS = "Unknown Linux distribution"

print(device_CPU)
print(device_OS)
print("Welcome to the Python CPU Benchmark Program! In this program, your computer's single-threaded performance will be tested by doing various math calculations.")

time.sleep(5)
count = 11
for i in range(10):
    count -= 1
    print(f"The benchmark will begin in {count} seconds")
    time.sleep(1)

start = datetime.datetime.now()
for a in range(5000000000):
    if a%10 == 0:
        if a%8 == 0:
            if a%6 == 0:
                if a %4 == 0:
                    if a%2 == 0:
                        print(a)

end = datetime.datetime.now()
print(f"Benchmark started at:")
print(start.strftime("%X"))
print(f"Benchmark ended at:")
print(end.strftime("%X"))