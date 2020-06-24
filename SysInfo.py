import PySimpleGUI as sg
import os, pathlib,sys
import cpuinfo
import psutil
import platform
import subprocess
from datetime import datetime
from system_info import sysinfo



'''
nnn = str(subprocess.check_output('wmic sounddev get Manufacturer,ProductName,Status', stderr=open(os.devnull, 'w'), shell=True)).split('\\r\\r\\n')

for n in nnn:
    if n != '' or n == "'":
        print(" ".join(n.split()))

'''


system_hardware_details = sysinfo.sysInfo
cinfo = cpuinfo.get_cpu_info()
uname = platform.uname()
#print(system_hardware_details)
#print(cinfo)

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
        



'''
print(f"Manufacturer\t: {system_hardware_details['Manufacturer']}")
print(f"Model\t\t: {system_hardware_details['Model']}")
print(f"Serial No\t: {system_hardware_details['Serial_Number']}")
print(f"Processor\t: {system_hardware_details['Processor']}")
print(f"Family Name\t: {uname.processor}")
print(f"CPU Core No\t: {system_hardware_details['CPU_Core']}")
print(f"Architecture\t: {cinfo['arch']}")
print(f"Bits\t\t: {cinfo['bits']}")
print(f"L2 Cache Size\t: {cinfo['l2_cache_size']}")
print(f"L3 Cache Size\t: {cinfo['l3_cache_size']}")
print(f"OS\t\t: {system_hardware_details['Operating System']}")
print(f"IP\t\t: {system_hardware_details['Ip']}")
print(f"Hostname\t: {system_hardware_details['Host Name']}")
print(f"Ram Type\t: {system_hardware_details['Ram_Type']}")
print(f"Ram Size\t: {system_hardware_details['Ram_Size']}")
#print(system_hardware_details)
#CPU INFORMATION
#cinfo = cpuinfo.get_cpu_info()
#print(cinfo)



# System Information
print("="*40, "System Information", "="*40)
print(f"System\t\t: {uname.system}")
print(f"Computer Name\t: {uname.node}")
print(f"Release\t\t: {uname.release}")
print(f"Version\t\t: {uname.version}")
print(f"Machine\t\t: {uname.machine}")
print(f"Processor\t: {uname.processor}")
# Boot Time
print("="*40, "Boot Time", "="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
# CPU Information
# let's print CPU information
print("="*40, "CPU Info", "="*40)
# number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")

# Memory Usage
# Memory Information
print("="*40, "Memory Information", "="*40)
# get the memory details
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")
print("="*20, "SWAP", "="*20)
# get the swap memory details (if exists)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")

# Disk Information
print("="*40, "Disk Information", "="*40)
print("Partitions and Usage:")
# get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    print(f"  Total Size: {get_size(partition_usage.total)}")
    print(f"  Used: {get_size(partition_usage.used)}")
    print(f"  Free: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")

# Network information
print("="*40, "Network Information", "="*40)
# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")
# get IO statistics since boot
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
'''
svmem = psutil.virtual_memory()
swap = psutil.swap_memory()
disk_io = psutil.disk_io_counters()
net_io = psutil.net_io_counters()

def ipinfo():
    if_addrs = psutil.net_if_addrs()
    ipread=""
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            ipread +="=== Interface: "+interface_name+" ===\n"
            if str(address.family) == 'AddressFamily.AF_INET':
                ipread +="  IP Address: "+str(address.address)+"\n"
                ipread +="  Netmask: "+str(address.netmask)+"\n"
                ipread +="  Broadcast IP: "+str(address.broadcast)+"\n"
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                ipread +="  MAC Address: "+str(address.address)+"\n"
                ipread +="  Netmask: "+str(address.netmask)+"\n"
                ipread +="  Broadcast MAC: "+str(address.broadcast)+"\n"
    return ipread
            
    
def diskinfo():
    rread=""
    # Disk Information
    #print("="*40, "Disk Information", "="*40)
    #print("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        #print(f"=== Device: {partition.device} ===")
        #print(f"  Mountpoint: {partition.mountpoint}")
        #print(f"  File system type: {partition.fstype}")
        rread +="=== Device: "+partition.device+"===\n"
        rread +="  Mountpoint: "+partition.mountpoint+"\n"
        rread +="  File system type: "+partition.fstype+"\n"
        
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        #print(f"  Total Size: {get_size(partition_usage.total)}")
        #print(f"  Used: {get_size(partition_usage.used)}")
        #print(f"  Free: {get_size(partition_usage.free)}")
        #print(f"  Percentage: {partition_usage.percent}%")
        rread +="  Total Size: "+get_size(partition_usage.total)+"\n"
        rread +="  Used: "+get_size(partition_usage.used)+"\n"
        rread +="  Free: "+get_size(partition_usage.free)+"\n"
        rread +="  Percentage: "+str(partition_usage.percent)+"% \n"
    # get IO statistics since boot
    #disk_io = psutil.disk_io_counters()
    #print(f"Total read: {get_size(disk_io.read_bytes)}")
    #print(f"Total write: {get_size(disk_io.write_bytes)}")

    return rread

    

def main():
    sg.theme('LightGrey3')  # No gray windows please!

    # STEP 1 define the layout
    tab1_layout =  [
                    [sg.T('Manufacturer\t'),sg.T(':'),sg.T(system_hardware_details['Manufacturer'])],
                    [sg.T('Model\t\t'),sg.T(':'),sg.T(system_hardware_details['Model'])],
                    [sg.T('Serial\t\t'),sg.T(':'),sg.T(system_hardware_details['Serial_Number'])],
                    [sg.T('Processor\t'),sg.T(':'),sg.T(system_hardware_details['Processor'])],
                    [sg.T('Family Name\t'),sg.T(':'),sg.T(uname.processor)],
                    [sg.T('CPU Core No\t'),sg.T(':'),sg.T(system_hardware_details['CPU_Core'])],
                    [sg.T('CPU Thread No\t'),sg.T(':'),sg.T(system_hardware_details['CPU'])],
                    [sg.T('Architecture\t'),sg.T(':'),sg.T(cinfo['arch'])],
                    [sg.T('Bits\t\t'),sg.T(':'),sg.T(cinfo['bits'])],
                    [sg.T('L1 Cache Size\t'),sg.T(':'),sg.T(str(cinfo['l2_cache_line_size'])+' KB')],
                    [sg.T('L2 Cache Size\t'),sg.T(':'),sg.T(cinfo['l2_cache_size'])],
                    [sg.T('L3 Cache Size\t'),sg.T(':'),sg.T(cinfo['l3_cache_size'])],
                    [sg.T('OS\t\t'),sg.T(':'),sg.T(system_hardware_details['Operating System'])],
                    [sg.T('HostName\t'),sg.T(':'),sg.T(system_hardware_details['Host Name'])],
                    ]

    tab2_layout = [
                    [sg.T('Ram Type\t'),sg.T(':'),sg.T(system_hardware_details['Ram_Type'])],
                    [sg.T('=========PHYSICAL MEMORY==========')],
                    [sg.T('Total\t\t'),sg.T(':'),sg.T(get_size(svmem.total))],
                    [sg.T('Available\t\t'),sg.T(':'),sg.T(get_size(svmem.available))],
                    [sg.T('Used\t\t'),sg.T(':'),sg.T(get_size(svmem.used))],
                    [sg.T('Percentage\t'),sg.T(':'),sg.T(str(svmem.percent)+"%")],
                    [sg.T('=========SWAP MEMORY==============')],
                    [sg.T('Total\t\t'),sg.T(':'),sg.T(get_size(swap.total))],
                    [sg.T('Available\t\t'),sg.T(':'),sg.T(get_size(swap.free))],
                    [sg.T('Used\t\t'),sg.T(':'),sg.T(get_size(swap.used))],
                    [sg.T('Percentage\t'),sg.T(':'),sg.T(str(swap.percent)+"%")],

                    ]
    tab3_layout = [
                    [sg.Multiline(default_text=diskinfo(), disabled=True, autoscroll=False, size=(50,10))],
                    [sg.T('Total Read'),sg.T(':'),sg.T(get_size(disk_io.read_bytes))],
                    [sg.T('Total Write'),sg.T(':'),sg.T(get_size(disk_io.write_bytes))],
                    ]
    tab4_layout = [
                    [sg.Multiline(default_text=ipinfo(), disabled=True, autoscroll=False, size=(50,10))],
                    [sg.T('Total Bytes Sent\t\t'),sg.T(':'),sg.T(get_size(net_io.bytes_sent))],
                    [sg.T('Total Bytes Received\t'),sg.T(':'),sg.T(get_size(net_io.bytes_recv))],
                    ]


    layout = [
                [sg.TabGroup([[sg.Tab('CPU Information', tab1_layout),
                               sg.Tab('Memory Information', tab2_layout),
                               sg.Tab('Disk Information', tab3_layout),
                               sg.Tab('Network Information', tab4_layout)]])],
                [sg.Button('Exit')]
             ]

    #STEP 2 - create the window
    window = sg.Window('Computer Information', layout, no_titlebar=True, grab_anywhere=True)

    # STEP3 - the event loop
    while True:
        event, values = window.read()   # Read the event that happened and the values dictionary
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
            break
        if event == 'Button':
          print('You pressed the button')
    window.close()

if __name__ == '__main__':
    main()
    


    
