import socket

# Crear un socket de cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor
server_address = ("localhost", 65432)
client_socket.connect(server_address)

try:
    # Enviar datos
    message = "Hola, servidor"
    minimun_number = int(input("Ingrese el número mínimo:"))
    maximun_number = int(input("Ingrese el número máximo" ":"))
    number_to_guess = int(input("Ingrese el número a adivinar" ":"))
    is_complete = input("Si no deseas jugar mas ingresa la palabra terminar de lo contrario dale enter para continuar" ":")
    print(f"Enviando: {message}")

    numbers = f"{minimun_number},{maximun_number},{number_to_guess},{is_complete}"
    client_socket.sendall(numbers.encode())
    # Esperar respuesta
    data = client_socket.recv(1024)
    print(f"Recibido del servidor: {data.decode()}")

finally:
    # Cerrar el socket
    client_socket.close()
