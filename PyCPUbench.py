import datetime
import time

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
