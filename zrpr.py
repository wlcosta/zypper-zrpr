#!/usr/bin/python3
import subprocess
import re

def treatInput(raw_input):
    #Removing the header
    m = re.sub(b'(((\w*\W)*\n*)\n(S \| (\w*\W*)\| (\w*\W*)\| (\w*))(\W)*\n)', b'', raw_input)

    x = []

    all_lines = m.splitlines()

    for all_shit in all_lines:
        s = re.search(b'((?:\w\W\|\W)(\w*)([\W*\w*_*-*].*))', all_shit)
        x.append(s.group(2).decode("utf-8"))
        '''s = re.search(b'((?:\w\W\|\W)(\w*)([\W*\w*_*-*].*))', m)
        x.append(s.group(2))
        re.sub(b'((?:\w\W\|\W)(\w*)([\W*\w*_*-*].*))', b'', m)'''

    return x

def getRawInput(repo_name):
    #string = subprocess.check_output(["zypper", "search", "--installed-only", "--repo", "Packman Repository"])
    string = subprocess.check_output(["zypper", "search", "--installed-only", "--repo", repo_name])

    return string
#This gets the string directly from zypper's output

packages = treatInput(getRawInput("Packman Repository"))

print("\nSo, this is the list of all packages: \n")
print(packages)

