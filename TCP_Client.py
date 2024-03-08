import socket


def tcp_client(target_host, target_port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            # Verbindung herstellen
            client.connect((target_host, target_port))
            # Daten senden
            client.sendall(request.encode())
            # Antwort empfangen
            response = client.recv(4096)
            print(response.decode())
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")


if __name__ == "__main__":
    target_host = "www.example.com"
    target_port = 80
    request = "GET / HTTP/1.1\r\nHost: example.com\r\nUser-Agent: MyTCPClient/1.0\r\n\r\n"
    tcp_client(target_host, target_port, request)
