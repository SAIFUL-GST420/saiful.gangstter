import os, sys

os.system('clear')

os.system('git pull')

try:

    __import__("saiful.gan").gangstter.saiful()

except Exception as e:

    exit(str(e))

 







