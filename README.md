Campus Announcement System

1. Project Overview

The Campus Announcement System is a Python-based client-server application that allows a campus administrator to send announcements to multiple connected students simultaneously.

The system uses TCP sockets for network communication and multithreading to handle multiple client connections.

2. Project Objectives

- Establish communication between a server and multiple clients.
- Use Python sockets for TCP communication.
- Apply multithreading to handle multiple student connections.
- Broadcast campus announcements to connected clients.
- Test the system with multiple clients.

3. Project Files

- "server.py": Starts the server, accepts client connections, and broadcasts announcements.
- "client.py": Connects a student to the server and displays received announcements.
- "README.md": Provides project documentation and execution instructions.

4. Technologies Used

- Python 3
- "socket" module
- "threading" module
- TCP/IP networking

The "socket" and "threading" modules are included in the Python standard library.

5. How the System Works

1. The administrator starts the server.
2. Students run the client program and enter their usernames.
3. Each client connects to the server using TCP.
4. The server creates a separate thread to handle each client connection.
5. The administrator types an announcement in the server terminal.
6. The server broadcasts the announcement to all currently connected clients.
7. Each client displays the announcement in its terminal.

6. How to Run the Program

Step 1: Check Python

Make sure Python 3 is installed on your computer.

Step 2: Start the Server

Open a terminal in the project directory and run:

python server.py

Step 3: Start the Clients

Open separate terminal windows and run:

python client.py

Enter a username in each client terminal.

Step 4: Send an Announcement

Type an announcement in the server terminal and press Enter. Connected clients should receive the message.

Step 5: Stop the Server

Type "/quit" in the server terminal and press Enter.

7. Testing

The system should be tested with multiple clients connected simultaneously.

Suggested tests:

- Connect two or more clients.
- Send an announcement and verify that all connected clients receive it.
- Disconnect a client and check that the server continues running.
- Verify that an empty username is rejected by the client.

Record the actual test results and include screenshots as evidence.

## System Architecture

![Campus Announcement System Architecture](docs/Dr.png)

8. Conclusion

The Campus Announcement System demonstrates TCP socket communication, multithreading, and message broadcasting in Python. It provides a simple example of how a server can distribute announcements to multiple connected clients.

Note: The current client configuration uses "127.0.0.1", so the client and server can be tested on the same computer. For clients on other computers, configure the client to use the server computer's reachable IP address.
