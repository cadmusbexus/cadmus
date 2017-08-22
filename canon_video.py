
# Importing all packages.
import subprocess, signal, os
import time
from time import sleep

# Killing the process before starting the routine.
p = subprocess.Popen(['ps', '-A'], stdout = subprocess.PIPE)
out, err = p.communicate()

for line in out.splitlines():
    if b'gvfsd-gphoto2' in line:
        # Kill the process!
        pid = int(line.split(None,1)[0])
        os.kill(pid, signal.SIGKILL)

# Infinite loop that will continuously take pictures.
while True:
    # Burstmode during 10seconds.
    p = subprocess.Popen(['gphoto2', '--set-config', 'eosviewfinder=1', '--wait-event=500ms', '--set-config', 'movierecordtarget=0', '--wait-event=10s'])
    out = p.communicate()
    # Sleep during a 1s.
    sleep(1)


    # Burstmode during 10seconds.
    p = subprocess.Popen(['gphoto2', '--set-config', 'eosviewfinder=1', '--wait-event=500ms', '--set-config', 'movierecordtarget=0', '--wait-event=10s'])
    out = p.communicate()

    # Compute the number of files in the folder. 
    s = subprocess.Popen(['gphoto2',"--num-files", "--folder=/store_00020001/DCIM/101CANON"], stdout=subprocess.PIPE)
    out,err = s.communicate()

    # Get the number of files.
    p = str(out[59:-1],'utf-8')

    # Download the last picture (the number of the picture = number of files).
    r = subprocess.Popen(['gphoto2',"--get-file="+p, "--folder=/store_00020001/DCIM/101CANON"])
    out = r.communicate()






