# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
from requests import get

def get_ip():
    # Use a breakpoint in the code line below to debug your script.
    print(os.system('ifconfig'))
    ip = get('https://api.ipify.org').content.decode('utf-8')
    print("public ip is : {}".format(ip))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_ip()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
