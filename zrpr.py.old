#!/usr/bin/python3
import subprocess
repo = str(input('Insert repo name: '))
string = subprocess.check_output(["zypper", "search", "--installed-only", "--repo", repo])
'''unmerge = str(input('Do you want to remove packages that appear in some other repo?\nIf yes, type in the repository name'))
if not unmerge:
    print("OK! No repositories will be considered...")

'''
all_description = []
#all_description = string.replace("b'Loading repository data...", "").replace("Reading installed packages...", "").replace("\n\n\nS | Name                                 | Summary                  | Type   \n--+--------------------------------------+--------------------------+--------\n", "").replace(split('|')
all_description = str(string).replace("b'Loading repository data...\\nReading installed packages...\\n\\nS | Name               | Summary                                                 | Type   \\n--+--------------------+---------------------------------------------------------+--------\\n", "").split('|')
packages = []
# How many packages are there?

import math
total_pkg = math.floor(len(all_description)/3)
aid = 1
for idx,notSureIfPackage in enumerate(all_description):
    
    while aid < len(all_description):
        packages.append(all_description[aid].replace(" ", ""))
        aid = aid+3
    
    packages
    #print("end")

zypp = ""
for pkg in packages:
    zypp = zypp+" "+pkg

print("sudo zypper rm"+zypp)
