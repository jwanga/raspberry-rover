# raspberry-rover
A Raspberry Pi powered, Wiimote controlled rover.

##Prerequisites
- A Wii Remote
- 

##Instalation
clone this repository into the /home directory of your raspberry pi.
```sh
cd /home
git clone https://github.com/jwanga/raspberry-rover.git
```


### Creating a service
We want the rover software to run when the Pi boots and blutooth becomes availible. Consequently we create an autorestarting service by creating the following file:
```sh
sudo nano /lib/systemd/system/raspberry-rover.service
```

Within that file add the following:
```
[Unit]
Description=Raspberry Rover
After=multi-user.target
 
[Service]
Type=simple
ExecStart=/usr/bin/python /home/raspberry-rover/main.py
Restart=on-abort
 
[Install]
WantedBy=multi-user.target
```

After the service is created, we activate it with the following:
```sh
sudo chmod 644 /lib/systemd/system/raspberry-rover.service
chmod +x /home/raspberry-rover/main.py
sudo systemctl daemon-reload
sudo systemctl enable raspberry-rover.service
sudo systemctl start raspberry-rover.service
```

###Maintenence

The following commands maintain and monitor the service.
```sh
# Check status
sudo systemctl status raspberry-rover.service
 
# Start service
sudo systemctl start raspberry-rover.service
 
# Stop service
sudo systemctl stop raspberry-rover.service
 
# Check service's log
sudo journalctl -f -u raspberry-rover.service
```
