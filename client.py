import socket

# Client socket configuration
host = "127.0.0.1"
port = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Receive welcome message from server
data = client.recv(1024)
print(data.decode())

# Get user input and send vote to server
while True:
    print("Please enter your vote (option1/option2/option3):")
    vote = input()
    client.send(vote.encode())
    response = client.recv(1024)
    print(response.decode())
