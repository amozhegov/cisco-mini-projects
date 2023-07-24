from gpio import *
from time import *

sensor = 0
pantalla = 1

def main():
	pinMode(1, OUT)
	print('Push button for attention!')
	while True:
		if digitalRead(sensor):
			customWrite(pantalla, 'ATTENTION!')
		delay(5000)
		customWrite(pantalla, '')

if __name__ == '__main__':
	main()