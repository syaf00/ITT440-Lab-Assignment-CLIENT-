import os
from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.56.104',  #VM server IP
    'username': 'syaf00', #server username
    'password': 'Syaf120601', #server password
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)

output = net_connect.send_command('apt-get update')
os.system(output)
print(output)
