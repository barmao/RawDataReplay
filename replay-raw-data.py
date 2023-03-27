import socket
import sys

# Define the host and port you want to connect to
HOST = sys.argv[1]
PORT = int(sys.argv[2])

# Create a TCP socket and connect to the specified host and port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Get log file
filename = sys.argv[3]
lines = []

with open(filename, "r") as file:
    for line in file:
        if "<" in line:            
            sock.sendall(bytes.fromhex(line.split("HEX: ")[-1]))
            sock.recv(2048)
            
# Close the socket when done
sock.close()
