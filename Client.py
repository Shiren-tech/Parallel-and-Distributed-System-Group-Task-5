import socket 

HOST = "127.0.0.1"
PORT = 5000

def main():
    username = input("Enter you Name: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:
        client_socket.connect((HOST, PORT))

        client_socket.sendall(username.encode("utf-8"))

        print(f"Connected as {username}!")
        print("Waiting for campus announcements...\n")

        while True:
            data = client_socket.recv(10234)

            if not data:
                print("Server disconnected.")
                break

            message = data.decode("utf-8")
            print(message, end="", flush=True)

    except ConnectionRefusedError:
        print("Could not connect. Make sure the server is running.")

    except OSError as error:
        print(f"Connection error: {error}")

    finally:
        client_socket.close()

if __name__=="__main__":
    main()