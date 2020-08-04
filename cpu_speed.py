"""
mac系统和windows系统的代码没有经过实际运行，并不知道是否能成功
"""
import platform
import subprocess
import fileinput


#获得mac系统cpu的速度
def get_mac_cpu_speed():
    commond = 'system_profiler SPHardwareDataType | grep "Processor Speed" | cut -d ":" -f2'
    proc = subprocess.Popen([commond], shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    output = output.decode()
    speed = output.lstrip().rstrip('\n')
    return speed


#获取Linux系统cpu的速度
def get_linux_cpu_speed():
    for line in fileinput.input('/proc/cpuinfo'):
        if 'MHz' in line:
            value = line.split(':')[1].strip()
            value = float(value)
            speed = round(value / 1024, 1)
            return "{speed} GHz".format(speed=speed)


#获取windows系统cpu的速度
def get_windows_cpu_speed():
    import winreg
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
    speed, type = winreg.QueryValueEx(key, "-MHz")
    speed = round(float(speed) / 1024, 1)
    return "{speed} GHz".format(speed=speed)


#判断系统的类型，并返回正确的值
def get_cpu_speed():
    osname = platform.system()
    speed = ''
    if osname == "Darwin":
        speed = get_mac_cpu_speed()
    if osname == "Linux":
        speed = get_linux_cpu_speed()
    if osname in ["Windows", "Win32"]:
        speed = get_windows_cpu_speed()
    return speed


print(get_cpu_speed())
