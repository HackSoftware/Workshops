# Synchronous echo server
import socket


def echo_handler(connection, addr):
    """
    Data is read from the connection with recv() and transmitted with sendall().
    """
    print('Connection from ', addr)

    # Receive the data in small chunks and retransmit it
    with connection:
        while True:
            data = connection.recv(1000)

            if not data:
                break

            connection.sendall(data)

    print('Connection closed.')


def echo_server(address):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Running several times with too small delay between executions,
    # could lead to: socket.error: [Errno 98] Address already in use
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # Associate the socket with the provided server address
    sock.bind(address)
    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        connection, addr = sock.accept()
        # accept() returns an open connection between the server and client + the
        # address of the client. The connection is different socket on another port
        echo_handler(connection, addr)


echo_server(('', 25000))  # '' -> localhost
