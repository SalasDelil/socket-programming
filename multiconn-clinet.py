import socket

SERVER = '192.168.0.6'
PORT = 5050

client_name = input("Enter client name: ")
number = int(input('Enter an integer between 1 and 100: '))


def client_handler():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    
    name = f'Client of {client_name}'
    message = f'{name}:{number}'
    client.send(message.encode())
    
    data = client.recv(1024).decode()
    
    server_name, server_number = data.split(':')
    server_number = int(server_number)
    
    # Print the client name, server name, and sum of the numbers
    total = number + server_number
    print(f'{server_name} connected to {name}.')
    print(f'Client number: {number}')
    print(f'Server number: {server_number}')
    print(f'Total: {total}')
    
    client.close()
    

client_handler()
