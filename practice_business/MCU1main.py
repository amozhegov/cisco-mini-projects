from gpio import *
from time import *

sensor = 0
puerta = 1

def main():
	pinMode(sensor, IN)
	print('Apertura de puerta')
	while True:
		if digitalRead(sensor):
			customWrite(puerta, '1') #abrir 
			print('Puerta Abierta')
		else:
			customWrite(puerta, '0') #cierra la puerta
			print('Puerta cerrada')
		
		delay(1000)
		
if __name__ == '__main__':
	main()