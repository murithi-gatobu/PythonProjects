import socket
import struct

MULTICAST_GROUP = '224.1.1.1'
PORT = 5007

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
ttl = struct.pack('b', 1)  # Local network only
server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

print(f"Multicast server sending to {MULTICAST_GROUP}:{PORT}")
print("Type your message and press Enter to send. Type 'exit' to quit.")

while True:
    message = input(">> ")
    if message.lower() == 'exit':
        print("Shutting down server.")
        break
    server_socket.sendto(message.encode(), (MULTICAST_GROUP, PORT))
    print(f"Sent: {message}")