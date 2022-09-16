# Netmiko basic script

from netmiko import ConnectHandler

cisco = {
    'device_type': 'cisco_ios',
    'host': '192.168.159.171',
    'username': 'skills',
    'password': 'nacional?2021',
}

commands = ['do sh ip int br',
            'do sh ipv6 int br',
            'do show ip route',
            'do sh ipv6 route']
connect = ConnectHandler(**cisco)
print(connect.find_prompt())
#output = connect.send_config_from_file('config.txt')  # Usar um arquivo externo como referencia de comandos
#output = connect.send_command('sh ip int br') # usa apenas um comando por vez
output = connect.send_config_set(commands)  #referencia à variavel "commands"
print(output)

