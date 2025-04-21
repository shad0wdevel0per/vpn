import socket
import ssl

HOST = '0.0.0.0'
PORT = 4433

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')  # Gere com openssl

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"[🔐] Servidor VPN escutando em {HOST}:{PORT}...")

    with context.wrap_socket(sock, server_side=True) as ssock:
        while True:
            conn, addr = ssock.accept()
            print(f"[📡] Conexão de {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"[🔁] Dados recebidos: {data.decode()}")
                conn.sendall(data)  # Echo