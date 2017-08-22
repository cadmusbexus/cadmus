# Importing all packages.
import subprocess, signal, os
import time
from time import sleep

# Killing the process before starting the routine.
p = subprocess.Popen(['ps', '-A'], stdout = subprocess.PIPE)
out, err = p.communicate()

# Delecting all existing files before taking pictures.
p = subprocess.Popen(['gphoto2', '--folder', '/store_00020001/DCIM/100CANON', '-R', '--delete-all-files'])
out = p.communicate()











