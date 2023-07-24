function setup() {
	pinMode(0, INPUT);
	pinMode(1, INPUT);
	pinMode(2, OUTPUT);
	pinMode(3, OUTPUT);
	pinMode(4, OUTPUT);
	pinMode(5, OUTPUT);
}

function loop() {

	var poten = analogRead(A0);
	var flex = analogRead(A1);

	if(digitalRead(1) == HIGH){
		digitalWrite(3, HIGH);
	} else {
		digitalWrite(3, LOW);
	}

	if(digitalRead(0) == HIGH){
		customWrite(2, '2');
	} else {
		customWrite(2, '0');
	}
	
	if(poten > 100){
		customWrite(4, '1');
	} else {
		customWrite(4, '0');
	}
	
	if(flex > 0){
		digitalWrite(5, HIGH);
	} else {
		digitalWrite(5, LOW);
	}
//analogWrite(flex);
}
