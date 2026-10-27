# Campus Announcement System

A Python-Based Client-Server Application Using TCP Sockets and Multithreading

## 1. Project Overview

The Campus Announcement System is a Python-based client-server application designed to simulate a university announcement service. It enables a campus administrator to distribute announcements to multiple connected students simultaneously.

The system uses TCP sockets for network communication and multithreading to handle multiple client connections concurrently. It demonstrates fundamental concepts of parallel and distributed systems, including concurrent processing, client-server communication, and message broadcasting.

## 2. Project Objectives

The main objectives of this project are to:

- Establish communication between one server and multiple clients.
- Implement TCP socket communication using Python.
- Apply multithreading to handle multiple client connections concurrently.
- Broadcast campus announcements to connected clients.
- Validate usernames before establishing a client session.
- Test client connections, announcement delivery, disconnection handling, and server shutdown.
- Demonstrate fundamental principles of distributed systems.

## 3. System Architecture

The system follows a client-server architecture in which one server manages multiple connected clients.

### Main Components

- **Campus Administrator:** Enters announcements through the server terminal.
- **Server (`Server.py`):** Accepts client connections, manages connected clients, and broadcasts announcements.
- **Client (`Client.py`):** Connects to the server, submits a username, and displays received announcements.
- **TCP Sockets:** Provide reliable, connection-oriented network communication.
- **Threads:** Allow the server to handle multiple client connections concurrently.
- **Client Registry:** Stores active client connections and their associated usernames.

### Architecture Diagram

![Campus Announcement System Architecture](docs/Dr.png)

### Communication Flow

1. The server starts and listens on port `5000`.
2. A client connects to the server through a TCP socket.
3. The client submits a username.
4. The server registers the client and creates a dedicated thread to handle its connection.
5. The administrator enters an announcement in the server terminal.
6. The server broadcasts the announcement to registered clients.
7. Each connected client displays the announcement.
8. When a client disconnects, the server attempts to remove its connection from the client registry.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| `socket` | TCP network communication |
| `threading` | Concurrent client handling |
| TCP/IP | Reliable transport between server and clients |
| Git and GitHub | Version control and collaboration |

The `socket` and `threading` modules are included in Python's standard library and do not require separate installation.

## 5. Project Structure

The project files are organized as follows:

```text
Campus-Announcement-System/
├── Server.py
├── Client.py
├── README.md
└── docs/
    ├── Dr.png
    ├── 18552327-10-2026 القطة شاشة.png
    ├── 185555 27-10-2016 لقطة شاشة.png
    ├── 185631 27-10-2016 لقطة شاشة.png
    ├── 185649 27-10-2026 القطة شاشة.png
    └── 185711 27-10-2026- لقطة شاشة.png
```

**Note:** Ensure that the actual file names, including dates, spaces, punctuation, and spelling, match the names used in this document.

## 6. How the System Works

### 6.1 Server Initialization

The server creates a TCP socket, enables address reuse, binds to `0.0.0.0` on port `5000`, and starts listening for incoming client connections.

### 6.2 Client Connection

Each client connects to the server and sends a username. The server validates the received username and registers valid clients.

### 6.3 Concurrent Client Handling

The server creates a separate thread for each accepted client connection. This allows the server to accept additional clients while existing connections are being handled.

### 6.4 Announcement Broadcasting

The administrator enters an announcement through the server terminal. The server sends the announcement to clients registered as connected.

### 6.5 Client Disconnection

The server monitors each client connection to detect when the connection closes or an error occurs. The connection is then removed from the client registry during cleanup.

### 6.6 Server Shutdown

The administrator can enter `/quit` to stop the server. The server closes the listening socket and attempts to close the remaining client connections.

## 7. How to Run the Program

### Prerequisites

- Python 3 installed on the computer.
- The project files available locally.
- A terminal or command-line interface.

### Step 1: Start the Server

Open a terminal in the project directory and run:

```bash
python Server.py
```

The server should display messages similar to:

```text
Campus Announcement Server Started!
Listening on port 5000
Type an announcement and press Enter.
Type /quit to stop the server.

Announcement>
```

Keep the server terminal running.

### Step 2: Start a Client

Open another terminal and run:

```bash
python Client.py
```

Enter a username when prompted.

Example:

```text
Enter you Name: Huda
Connected as Huda!
Waiting for campus announcements...
```

### Step 3: Start Additional Clients

Open a separate terminal for each additional client and run:

```bash
python Client.py
```

Enter a different username for each client.

### Step 4: Broadcast an Announcement

In the server terminal, enter an announcement:

```text
Announcement> The campus library will close at 5 PM today.
```

The connected clients should receive a message similar to:

```text
[CAMPUS ANNOUNCEMENT] The campus library will close at 5 PM today.
```

### Step 5: Stop the Server

Enter `/quit` in the server terminal and press Enter.

The server should display:

```text
Server stopped.
```

## 8. Testing and Results

The system was tested to evaluate multiple client connections, announcement broadcasting, username validation, client disconnection, and server shutdown.

| Test Case | Expected Result | Observed Result | Status |
|---|---|---|---|
| Multiple client connections | The server accepts multiple clients. | Multiple clients connected successfully. | Passed |
| Announcement broadcasting | Connected clients receive the same announcement. | Both clients received the announcement. | Passed |
| Empty username validation | The client rejects an empty username. | `Username cannot be empty.` was displayed. | Passed |
| Client disconnection | The server detects the disconnection and removes the client. | The server continued running, and the remaining client received a new announcement. The disconnection message was not observed immediately. | Partially Passed |
| Server shutdown | The server shuts down safely. | `Server stopped.` appeared after `/quit` was entered. | Passed |

### 8.1 Testing Observations

- Multiple clients connected to the server successfully.
- Announcement broadcasting worked for connected clients.
- Empty usernames were rejected before a connection was established.
- After one client was interrupted using `Ctrl + C`, the remaining client continued receiving announcements.
- The disconnection notification was not observed immediately and requires further investigation.
- The server shut down successfully when `/quit` was entered.

### 8.2 Screenshots of Test Results

The following screenshots provide visual evidence of the project implementation and testing process.

#### Screenshot 1: Initial System Test

![Initial System Test](docs/18552327-10-2026%20%D8%A7%D9%84%D9%82%D8%B7%D8%A9%20%D8%B4%D8%A7%D8%B4%D8%A9.png)

#### Screenshot 2: Client Connection Test

![Client Connection Test](docs/185555%2027-10-2016%20%D9%84%D9%82%D8%B7%D8%A9%20%D8%B4%D8%A7%D8%B4%D8%A9.png)

#### Screenshot 3: Announcement Broadcasting Test

![Announcement Broadcasting Test](docs/185631%2027-10-2016%20%D9%84%D9%82%D8%B7%D8%A9%20%D8%B4%D8%A7%D8%B4%D8%A9.png)

#### Screenshot 4: Client Disconnection Test

![Client Disconnection Test](docs/185649%2027-10-2026%20%D8%A7%D9%84%D9%82%D8%B7%D8%A9%20%D8%B4%D8%A7%D8%B4%D8%A9.png)

#### Screenshot 5: Final System Test

![Final System Test](docs/185711%2027-10-2026-%20%D9%84%D9%82%D8%B7%D8%A9%20%D8%B4%D8%A7%D8%B4%D8%A9.png)

**Note:** The screenshot headings describe the testing evidence section. Confirm that each image actually shows the test described by its heading before submitting the report.

## 9. Limitations

The current implementation has several limitations:

- **Localhost configuration:** The client uses `127.0.0.1`, which is suitable for running the server and clients on the same computer.
- **Network configuration:** Connecting clients from other computers requires changing the client host address to the server computer's reachable IP address and ensuring that port `5000` is accessible.
- **Basic username handling:** The system does not implement authentication or identity verification.
- **Unencrypted communication:** Messages are transmitted without application-level encryption.
- **Disconnection notification:** The disconnection notification was not observed immediately during testing and requires further investigation.
- **Basic message protocol:** The implementation uses TCP streams without an explicit message-framing protocol.

## 10. Future Improvements

Potential improvements include:

- Implementing robust message framing and username validation.
- Improving detection and logging of disconnected clients.
- Adding administrator authentication and access control.
- Adding timestamps and announcement categories.
- Improving error handling and connection management.
- Supporting clients on different computers over a local network.
- Adding automated tests and detailed logging.

## 11. Conclusion

The Campus Announcement System demonstrates a basic distributed application built with Python TCP sockets and multithreading.

The observed tests confirmed that multiple clients could connect to the server, receive the same announcement, and reject an empty username. The server also continued operating after a client disconnected and shut down successfully when instructed.

Although the prototype has limitations in connection management, message framing, and security, it provides a practical demonstration of client-server communication, concurrent processing, and announcement broadcasting in a campus environment.
