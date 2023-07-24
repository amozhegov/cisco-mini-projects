var port = 1234;
var dstIP = "192.168.1.1";
var socket;
var state ;
function setup() {
pinMode(0,INPUT);
state = 0;
socket = new UDPSocket();
// Recepcion UDP
socket.onReceive = function(ip, port, data) {
Serial.println("Recibido de "
+ ip + ":" + port + ": " + data);
};
// Activa el socket UDP en el puerto
Serial.println(socket.begin(port));
}
function loop() {
if (digitalRead(0)) {
if (state === 0) {
state = 1;
socket.send(dstIP, port, "1");
Serial.println("ON");
}
}
else{
if (state === 1) {
state = 0;
socket.send(dstIP, port, "0");
Serial.println("OFF");
}
}
delay(1000);
}