import socket
import random

# Crear un socket de servidor TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a la dirección y puerto
server_address = ("localhost", 65432)
server_socket.bind(server_address)

# Escuchar conexiones entrantes
server_socket.listen(5)
print(f"Servidor escuchando en {server_address}")

def adivinar_numero(minimo, maximo, numero_adivinar):
    coontador_desaciertos = 0
    
    while coontador_desaciertos <3:
        numero_aleatorio = random.randint(minimo, maximo)
        
        if numero_aleatorio == numero_adivinar:
            print(f"El número {numero_aleatorio} es el correcto")
            return True
        elif numero_aleatorio < numero_adivinar:
            print(f"El número {numero_aleatorio} es menor que el número que se quiere adivinar")
            minimo = numero_aleatorio +1
        elif numero_aleatorio > numero_adivinar:
            print(f"El número {numero_aleatorio} es mayor que el número que se quiere adivinar")
            maximo = numero_aleatorio -1
        
        coontador_desaciertos += 1
        print(f"Llevas {coontador_desaciertos} desacierto(s)")
    
    print(f"Perdiste, el número a adivinar era {numero_adivinar}")
    return False

cantidad_turnos_exitosos = 0
cantidad_turnos_fallidos = 0

while True:
    # Esperar a que un cliente se conecte
    print("Esperando conexión de un cliente...")
    connection, client_address = server_socket.accept()
    
    try:
        print(f"Conexión establecida con: {client_address}")

        # Recibir los datos en fragmentos
        data = connection.recv(1024)
        if data:
            received_message = data.decode()
            print(f"Recibido: {received_message}")

           
            # Separar los números usando el delimitador
            numbers_str = received_message.split(",")
            
            if len(numbers_str) >= 3:
                minimun_number = int(numbers_str[0])
                maximun_number = int(numbers_str[1])
                number_to_guess = int(numbers_str[2])
                print(f"Números recibidos: Min={minimun_number}, Max={maximun_number}, Adivinar={number_to_guess}") 
            
                if adivinar_numero(minimun_number, maximun_number, number_to_guess):
                    cantidad_turnos_exitosos += 1
                else:
                    cantidad_turnos_fallidos += 1
                
                if numbers_str[3] == "terminar":
                    connection.close()
                    break

                # Imprimir los contadores
                print(f"La cantidad de turnos exitosos es {cantidad_turnos_exitosos}")
                print(f"La cantidad de turnos fallidos es {cantidad_turnos_fallidos}")
               
            else:
                print("No se recibieron suficientes números.")

            # Responder al cliente
            connection.sendall(b"Mensaje recibido")
               
        else:
            print("No hay más datos del cliente")
   
    finally:
        if received_message == "0,0,0":
        # Cerrar la conexión
            connection.close()
  
