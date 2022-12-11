import datetime
import time
import platform as deviceinfo
import threading
import _thread

# NOTE: The threading and _thread modules are stubs. These will be used to add multi-threaded benchmarks in the future

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
while True:
    lengthinput = input("How long do you want the test to be?\nType \"Short\" for calculations up to 1,000,000,000.\nType \"Medium\" for calculations up to 5,000,000,000.\nType \"Long\" for calculations up to 10,000,000,000.\nPlease input your answer: ")
    if lengthinput == "Short":
        testlength = 1000000000
        break
    elif lengthinput == "Medium":
        testlength = 5000000000
        break
    elif lengthinput == "Long":
        testlength = 10000000000
        break
    else:
        print("Please input a valid answer.")
        continue

count = 11
for i in range(10):
    count -= 1
    print(f"The benchmark will begin in {count} seconds")
    time.sleep(1)

start = datetime.datetime.now()

for a in range(testlength):
    if a%10 == 0:
        if a%8 == 0:
            if a%6 == 0:
                if a %4 == 0:
                    if a%2 == 0:
                        print(a)

end = datetime.datetime.now()
results = end - start
start = str(start)
end = str(end)
results = str(results)

print(f"Benchmark length: {lengthinput}")
print(f"Benchmark started at: {start}")
print(f"Benchmark ended at: {end}")
print(f"Benchmark took: {results}")
print(f"System CPU: {device_CPU}")
print(f"Operating System: {device_OS}")