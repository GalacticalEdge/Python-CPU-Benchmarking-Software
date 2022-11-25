# NOTE: This is pre-development software and I plan to add more to this over time.

# Python CPU Benchmarking Software
A Python program that benchmarks the performance of the computer it runs on.

# How useful is this?
This program can be used to benchmark single-threaded performance. I, along with the help of friends, have tested this program on these CPUs:
| CPU  | Time |
| ------------- | ------------- |
| AMD Ryzen 5 5600X (AVX-256, Linux) | 5.15 Minutes  |
| Intel Core i7 9750H (AVX2, Windows) | 42.41 Minutes |
| Intel Core i5 1155G7 (AVX-512, Linux) | 8.14 Minutes  |
| Raspberry Pi 4 Model B 4GB (Linux) | 59.48 Minutes |

One of the best things of Python is that it often takes advantage of instruction set extensions on processors that support them, so this program can take advantage of them and show just how powerful your computer is.
# What do I plan to add over time?
* Multi-threaded benchmarks
* Improvements to the benchmarking
* Better intractability with the program

Do not expect these to come any time soon, since I am still a Python beginner who only knows the basics.

I will welcome any contributions to this project with open arms. If you happen to be seeing this, don't hesitate to look and help improve this software!

# How do I run this software?
It's easy, but it will depend on what computer you have. I have only tested this software with Python 3.10, so I won't be able to help if this doesn't work in any other version.

If you use Windows, download Python 3.10 from their [official website](https://www.python.org/) or from the Microsoft Store.

I do not know about MacOS, but I believe versions after MacOS 11 do not come with Python preinstalled. So again, go to Python's [official website](https://www.python.org/) to download Python 3.10.

If you use Linux (which this software was extensively tested on), download Python from your distro's repositories if you don't have it already installed. Some distros (like PopOS and Raspberry Pi OS) come with it preinstalled however.

After you've installed Python, download the code from this repository. After it's done, extract the files and open the terminal application on your computer (On Windows, it's Command Prompt. On MacOS, it's Terminal. On Linux, it will vary based on distro) and type "python3 (Path to PyCPUbench.py goes here)". Let it run and see the results! (Please note it may take awhile depending on how fast your computer's single-threaded performance is)

# License
The license can be found in the project's code. Please refer to it if you want to fork this project or borrow any code.
