var temp ={};
var hum = {}
var tasmota ={};

var led1 = {};
var led2 = {};

var array = msg.payload.split(',');
    temp.payload = parseFloat(array[0].slice(0,5)), 
    hum.payload = parseFloat(array[1].slice(0,5));
    
if (temp.payload >= 25 || hum.payload >= 2568) {
    tasmota.payload = 1;
    if (temp.payload >= 25){
        led1.payload = true;
    }
    else{
        led1.payload = false;
    }
    if (hum.payload >=2568){
        led2.payload = true;
    }
    else{
        led2.payload = false; 
    }
}
else {
    tasmota.payload = 0;
    led1.payload = false;
    led2.payload = false;
}
return [temp,led1,tasmota, hum, led2];