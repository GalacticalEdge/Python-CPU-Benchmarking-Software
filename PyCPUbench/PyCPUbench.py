import datetime
import time
import platform as deviceinfo

device_CPU = deviceinfo.processor()
if device_CPU == "":
    device_CPU = "Unknown processor"

device_OS = deviceinfo.system()
if device_OS == "Darwin":
    device_OS = "MacOS"
elif device_OS == "Linux":
    try:
        device_OS = deviceinfo.freedesktop_os_release()
        device_OS = device_OS["NAME"]
    except:
        device_OS = "Unknown Linux distribution. Please make sure /etc/os-release or /usr/lib/os-release can be read"
elif device_OS == "":
    device_OS = "Unknown operating system"

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
results = end - start
print("Benchmark started at: ", end="")
print(start.strftime("%X"))
print("Benchmark ended at: ", end="")
print(end.strftime("%X"))
print("Benchmark took: ", end="")
print(results)
print("System CPU: ", end="")
print(device_CPU)
print("Operating System: ", end="")
print(device_OS)
