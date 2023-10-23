import socket
import threading

# Dictionary to store votes
votes = {"option1": 0, "option2": 0, "option3": 0}

# Server socket configuration
host = "127.0.0.1"
port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

# Function to handle client requests
def handle_client(conn, addr):
    print(f"Connected to {addr}")
    conn.send(b"Welcome to Online Voting System!\n")

    while True:
        # Receive client vote
        data = conn.recv(1024)
        if not data:
            break
        vote = data.decode().strip().lower()

        # Update vote count
        if vote in votes:
            votes[vote] += 1
            response = f"Thank you for voting for {vote}!"
        else:
            response = "Invalid vote option!"

        # Send response to client
        conn.send(response.encode())

    # Close connection
    conn.close()
    print(f"Disconnected from {addr}")

# Listen for incoming connections
print(f"Listening on {host}:{port}...")
while True:
    conn, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
