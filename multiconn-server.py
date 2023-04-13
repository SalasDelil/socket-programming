import socket
import random

PORT = 5050
SERVER = ''
ADDR = (SERVER, PORT)


def server_handler():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f'Server listening...')

    while True:
        client, client_address = server.accept()
        data = client.recv(1024).decode()
        if not data:
            continue

        name, number = data.split(':')
        number = int(number)

        server_name = 'Server of Salas Delil'
        print(f'{name} connected to {server_name}.')

        server_number = random.randint(1, 100)
        total = number + server_number
        print(f"Client's random number: {number}")
        print(f"Server's number: {server_number}")
        print(f'Total sum : {total}')

        message = f'{server_name}:{server_number}'
        client.send(message.encode())
        client.close()

        print('/----------------------------------------------/\n')

        if number < 1 or number > 100:
            print('Terminating server.')
            server.close()
            break


server_handler()
