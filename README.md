# Remote-plant-monitoring-with-MQQT-and-two-ESP32s
![Imagen del proyecto](https://github.com/eduardofierropro/Portafolio-y-CV/blob/main/IMAGEN-DEL-PROYECTO.jpg?raw=true)

## Description 📑

This project was developed during my exchange year at the University of São Paulo (USP) and focused on monitoring a plant using IoT technology .The project consists of collecting data using an ESP32 microcontroller programmed with MicroPython and sending it via the MQTT protocol to a broker (HIVEMQ). The data is then read by nodered, where through a function it publishes the data in a dashboard and instructs the second ESP32 whether or not to open a valve depending on the sensor values. The second ESP32 microcontroller is flashed with tasmota and subscribed to a broker topic which allows it to send a code to activate a logic port. 

## What have I learned in this project? 🙇🏻 

During the project on the MQTT broker, I gained knowledge about the available technologies for ESP32 controllers, such as MicroPython and Tasmota. Additionally, I delved into the theory of the MQTT protocol and its practical implementation. I also had the opportunity to learn the basics of JavaScript, as the functions in Node-RED are developed in this language. Furthermore, I developed teamwork skills and overcame language barriers by collaborating with a colleague from Belgium and another from Switzerland.

## Technologies 🛠
![Python](https://a11ybadges.com/badge?logo=python)
![JavaScript](https://a11ybadges.com/badge?logo=javascript)
![Tasmota](https://a11ybadges.com/badge?logo=tasmota)
![Node-RED](https://a11ybadges.com/badge?logo=nodered)
## Vista previa del proyecto
Si quieres hechas un vistazo al proyecto, te recomiendo:

![Captura del proyecto](https://github.com/eduardofierropro/Portafolio-y-CV/blob/main/CAPTURA-DEL-PROYECTO.jpg?raw=true)
![Captura del proyecto](https://github.com/eduardofierropro/Portafolio-y-CV/blob/main/CAPTURA-DEL-PROYECTO.jpg?raw=true)
![Captura del proyecto](https://github.com/eduardofierropro/Portafolio-y-CV/blob/main/CAPTURA-DEL-PROYECTO.jpg?raw=true)

## Author ✒️
Cristopher Ricardo Escalante Hallasi

* [cristopherescalante@gmail.com](cristopherescalante@gmail.com)
* [LinkedIn](linkedin.com/in/cristopherescalante)

## Installation 

In order to run this project, you will need to install micropython on one ESP32, flash TASMOTA on the other. Then, load the JSON file in node red. Finally, configure the authorizations in your own MQQT broker.
  
## Licencia 📄
General Public License GNU v3
