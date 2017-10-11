# raspberry-rover
A Raspberry Pi powered, Wiimote controlled rover.


## Creating a servoce
We wante the rover software to run when the Pi boots. Consequently we create an autorestarting service by creating the following file:

```sh
sudo nano /lib/systemd/system/rover.service
```

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
