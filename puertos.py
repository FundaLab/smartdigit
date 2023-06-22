import serial

# Configuración del puerto serial
port = '/dev/ttyUSB1'  # Reemplaza con el nombre del puerto serial en tu sistema
baudrate = 9600

# Inicialización del puerto serial
ser = serial.Serial(port, baudrate)

while True:
    # Caracter a enviar
    char_to_send = "B"+input("Introduzca un numero")+"#"
    #'B7#'

# Envío del caracter
    ser.write(char_to_send.encode())

# Cierre del puerto serial
ser.close()
