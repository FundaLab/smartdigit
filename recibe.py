import serial

# Configuración del puerto serial
port = '/dev/ttyUSB1'  # Reemplaza con el nombre del puerto serial en tu sistema
baudrate = 9600

# Inicialización del puerto serial
ser = serial.Serial(port, baudrate)

# Bucle para leer continuamente los datos entrantes
while True:
    if ser.in_waiting > 0:
        # Leer la línea recibida y decodificarla
        line = ser.readline().decode().strip()
        
        # Mostrar la línea en la consola
        print(line)
