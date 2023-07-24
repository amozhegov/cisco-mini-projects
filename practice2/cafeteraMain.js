var port = 1234;
var dstIP = "192.168.1.2";

var socket;
function setup() {
socket = new UDPSocket();
customWrite(0,"0");
// Recepcion
socket.onReceive = function(ip, port, data) {
Serial.println("Recibido de "
+ ip + ":" + port + ": " + data);
if(data=="1"){
Serial.println("CAFETERA ENCENDIDA");
customWrite(0,"1");
}
else {
Serial.println("CAFETERA APAGADA");
customWrite(0,"0");
}
};
// Activa el socket UDP en el puerto
Serial.println(socket.begin(port));
}
function loop() {
// Nada
}
