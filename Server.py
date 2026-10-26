import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

clients = {}
clients_lock = threading.Lock()


def broadcast(message):
    """Send an announcement to all connected clients."""
    with clients_lock:
        connected_clients = list(clients.items())

    for client_socket, username in connected_clients:
        try:
            client_socket.sendall(
                (message + "\n").encode("utf-8")
            )
        except OSError:
            print(f"Could not send to {username}")


def handle_client(client_socket, address):
    """Handle one connected student."""
    username = None

    try:
        client_socket.settimeout(30)
        data = client_socket.recv(1024)

        if not data:
            return

        username = data.decode("utf-8").strip()

        if not username:
            return

        client_socket.settimeout(None)

        with clients_lock:
            clients[client_socket] = username

        print(f"{username} connected from {address}")
        client_socket.sendall(
            "Connected to Campus Announcement System!\n".encode("utf-8")
        )

        # Keep the connection alive and detect disconnections.
        while client_socket.recv(1024):
            pass

    except (OSError, UnicodeDecodeError):
        pass

    finally:
        with clients_lock:
            old_username = clients.pop(client_socket, None)

        client_socket.close()

        if old_username:
            print(f"{old_username} disconnected")


def accept_clients(server_socket):
    """Accept multiple student connections."""
    while True:
        try:
            client_socket, address = server_socket.accept()

            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address),
                daemon=True
            )
            thread.start()

        except OSError:
            break


def main():
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server_socket.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print("Campus Announcement Server Started!")
        print(f"Listening on port {PORT}")
        print("Type an announcement and press Enter.")
        print("Type /quit to stop the server.\n")

        accept_thread = threading.Thread(
            target=accept_clients,
            args=(server_socket,),
            daemon=True
        )
        accept_thread.start()

        while True:
            announcement = input("Announcement> ").strip()

            if announcement.lower() == "/quit":
                break

            if not announcement:
                continue

            broadcast(f"[CAMPUS ANNOUNCEMENT] {announcement}")
            print("Announcement broadcast completed.")

    except OSError as error:
        print(f"Server error: {error}")

    finally:
        server_socket.close()

        with clients_lock:
            connected_clients = list(clients.keys())
            clients.clear()

        for client_socket in connected_clients:
            try:
                client_socket.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
            client_socket.close()

        print("Server stopped.")


if __name__ == "__main__":
    main()