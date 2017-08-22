import psutil
import time
print(int(time.time()))
disk_usage = psutil.disk_usage('/')
print(disk_usage.percent)
print(psutil.cpu_percent(interval=1))
print(int(time.time())-psutil.boot_time())
