# NOTE: This is pre-development software and I plan to add more to this over time.

# Python CPU Benchmarking Software
A Python program that benchmarks the performance of the computer it runs on.

# How useful is this?
This program can be used to benchmark single-threaded performance. I along with the help of others have tested this program on these CPUs:
| CPU  | Time |
| ------------- | ------------- |
| Apple M1 (Mac Mini) | 4:46 |
| AMD Ryzen 5 5600X (AVX2, Linux) | 5:15 |
|  Intel Core i5 1155G7 (AVX-512, Linux) | 8:14 |
| Intel Core i7 9750H (AVX2, Windows) | 42:41 |
| Intel Core i5 9400F (AVX2, Windows) | 43:05 |
| Raspberry Pi 4 Model B 4GB (Linux) | 59:48 |
| Intel Core i5 6300U (AVX2, Windows) | 1:24:27 |

One of the best things of Python is that it often takes advantage of instruction set extensions (like AVX) on processors that support them, so this program can take advantage of them and show just how powerful your computer is.
# What do I plan to add over time?
* Multi-threaded benchmarks
* Improvements to the benchmarking
* Better intractability with the program

Do not expect these to come any time soon, since I am still a Python beginner who only knows the basics.

I will welcome any contributions to this project with open arms. If you happen to be seeing this, don't hesitate to look and help improve this software!

# How do I run this software?
It's easy, but it will depend on what computer you have. I have only tested this software with Python 3.10, so I won't be able to help if this doesn't work in any other version.

The instructions below are for if you do not have Python already installed. If you have Python installed, then you can skip to the last paragraph of this section.

If you use Windows, download Python 3.10 from their [official website](https://www.python.org/) or from the Microsoft Store.

I do not know about MacOS, but I believe versions after MacOS 11 do not come with Python preinstalled. So again, go to Python's [official website](https://www.python.org/) to download Python 3.10.

If you use Linux (which this software was extensively tested on), download Python from your distro's repositories if you don't have it already installed. Some distros (like Ubuntu) come with it preinstalled however. If your distro comes preinstalled with Python, it's recommended to not change or modify your operating system's built-in Python as that can break your operating system.

After you've installed Python, download the code from this repository. After it's done, extract the files and open the terminal application on your computer (On Windows, it's Command Prompt. On MacOS, it's Terminal. On Linux, it will vary based on distro) and type "python3 (Path to PyCPUbench.py goes here)". Let it run and see the results!

Note that it will take awhile depending how fast your system is. I recommend closing everything running in the background to minimize CPU and memory load.

# License
The license can be found in the project's code. Please refer to it if you want to fork this project or borrow any code.
