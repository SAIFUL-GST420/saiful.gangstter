import os, sys

os.system('clear')

os.system('git pull')

try:

    __import__("gan").gangstter.saiful()

except Exception as e:

    exit(str(e))

 







