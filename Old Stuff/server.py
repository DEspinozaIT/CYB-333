#!/usr/bin/env python3
"""Beginner TCP server for socket connection practice."""

import socket

HOST = "127.0.0.1"
PORT = 65432

# Create a socket and listen for a client connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Server is listening on {}:{}".format(HOST, PORT))

client_socket = None
try:
    client_socket, client_address = server_socket.accept()
    print("Client connected from", client_address)

    while True:
        data = client_socket.recv(1024)
        if not data:
            print("Client disconnected.")
            break

        message = data.decode("utf-8")
        print("Received from client:", message)

        if message.lower().strip() == "quit":
            client_socket.sendall("Server closing connection.".encode("utf-8"))
            print("Sent disconnect message.")
            break

        response = "Server received: " + message
        client_socket.sendall(response.encode("utf-8"))
        print("Sent response to client.")

except KeyboardInterrupt:
    print("\nServer stopped by user.")
finally:
    if client_socket:
        client_socket.close()
    server_socket.close()
    print("Server sockets closed.")
