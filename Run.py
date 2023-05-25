import os, platform

os.system('xdg-open  https://chat.whatsapp.com/LsJzNAVWxwwCrFqwmFYHBJ')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from MIX import mr_bean

    mr_bean()

elif bit == '32bit':

    print(50*"-")

    print("[>>] ONLY 64 BIT USERS CAN USE ")

    print(50*"-")

    exit()

