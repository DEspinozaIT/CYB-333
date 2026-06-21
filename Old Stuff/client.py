#!/usr/bin/env python3
"""Beginner TCP client for socket connection practice."""

import socket

HOST = "127.0.0.1"
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to {}:{}".format(HOST, PORT))
try:
    sock.connect((HOST, PORT))
    print("Connected to server.")

    while True:
        message = input("Enter message ('quit' to disconnect): ")
        if message == "":
            print("Please type something.")
            continue

        sock.sendall(message.encode("utf-8"))
        data = sock.recv(1024)
        if not data:
            print("Server closed the connection.")
            break

        reply = data.decode("utf-8")
        print("Reply from server:", reply)

        if message.lower().strip() == "quit":
            print("Disconnecting.")
            break

except ConnectionRefusedError:
    print("Could not connect. Make sure the server is running.")
except KeyboardInterrupt:
    print("\nClient stopped by user.")
finally:
    sock.close()
    print("Client socket closed.")
