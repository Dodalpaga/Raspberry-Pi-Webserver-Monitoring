# Raspberry-Pi-Webserver-Monitoring
## This repo regroups some monitoring projects of mine

You can find several files :
- ACCEL --> Gets the accelerometer data of my ObCP and stacks it into a DB
- Bluetooth --> Gets any information send through notifications of my "ObCP" (UUID 6e400003-b5a3-f393-e0a9-e50e24dcca9e) and stacks it into a DB
- CPU --> Gets your CPU/GPU info (CPU %, GPU %) and stacks it into a DB
- Network --> Gets your networks performances (Dwnl rate, upld rate, ping) and stacks it into a DB

The overall can be real-time monitored in a Grafana local server, by using the InfluxDB databases previously created

Note : The "ObCP" (Objet Connecté Programmable) is a home made microcontroller based on the STM32-L476-RG model from STMicroelectronics.
There are a few more components implemented on it : BLE, accelerometer, 3 colors LED, battery module, PWM output
