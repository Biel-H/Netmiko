NETMIKO basic creation tutorial

    This is a basic creation tutorial for Netmiko and how to use the automation
    from *Debian* to cisco router or cisco devices






## Python instalation 



```
apt install python3
```

### Install pip

```
apt install python3-pip or apt install pip
```

### Using pip install some packages for netmiko

```
pip download -d . SomePackage
```

### Now let's install the netmiko and paramiko

```
apt install build-essential libssl-dev libffi-dev -y
pip install netmiko
pip install paramiko
```

### SSH Debian to Router Configuration
    Inside of the /etc/ssh/ssh_config uncomment or add this line

`KexAlgorithms +diffie-helman-group-exchange-sha1, diffie-hellman-group14-sha1`

And now create the file with your code and execute!

```
To execute use the:
    python3 <name-of-the-file.py>
```

## Autors

- [@Biel-H](https://www.github.com/Biel-H)


## Documentation

[Docs](https://pyneng.readthedocs.io/en/latest/book/18_ssh_telnet/netmiko.html)

[Oficial Github](https://ktbyers.github.io/netmiko/docs/netmiko/cisco/index.html)