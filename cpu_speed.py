import platform
import subprocess
import fileinput


def get_mac_cpu_speed():
    commond = 'system_profiler SPHardwareDataType | grep "Processor Speed" | cut -d ":" -f2'
    proc = subprocess.Popen([commond], shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    output = output.decode()
    speed = output.lstrip().rstrip('\n')
    return speed


def get_linux_cpu_speed():
    for line in fileinput.input('/proc/cpuinfo'):
        if 'MHz' in line:
            value = line.split(':')[1].strip()
            value = float(value)
            speed = round(value / 1024, 1)
            return "{speed} GHz".format(speed=speed)


def get_cpu_speed():
    osname = platform.system()
    speed = ''
    if osname == "Darwin":
        speed = get_mac_cpu_speed()
    if osname == "Linux":
        speed = get_linux_cpu_speed()
    if osname in ["Windows", "Win32"]:
        print("Sorry, I can't get cpu's speed")
    return speed


print(get_cpu_speed())
