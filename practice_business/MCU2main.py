from gpio import *
from time import *

sensor = 0
garage = 1
ventana = 2
def main():
	pinMode(1, OUT)
	print('Abrir garage y ventana con boton')
	while True:
		if True:
			if digitalRead(sensor):
				customWrite(garage, '1')#abrir
				customWrite(ventana, '1')
				delay(5000)
			else:
				customWrite(garage, '0')#cerrar
				customWrite(ventana, '0')

if __name__ == '__main__':
	main()