#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space '''
# Author ID: ksingh631

import subprocess

def free_space():
    return subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, capture_output=True, text=True).stdout.strip()

if __name__ == '__main__':
    print(free_space())
