from gpio import *
from time import *

sensor = 0
puerta = 1
lamp = 2

def main():
	pinMode(sensor, IN) #pin de entrada
	customWrite(lamp, '0')
	print('Apertura de puerta')
	while True:
		if digitalRead(sensor):
			customWrite(puerta, '1')
			customWrite(lamp, '2')
			print('Puerta Abierta')
		else:
			customWrite(puerta, '0')
			print('Puerta cerrada')
		delay(1000)
		
if __name__ == '__main__':
	main()