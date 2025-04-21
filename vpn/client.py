import socket
import ssl

HOST = '127.0.0.1'  # IP do servidor
PORT = 4433

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  # Para testes, não exige CA

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        print("[🔌] Conectado ao servidor VPN (SSL)")
        while True:
            msg = input(">> Mensagem a enviar (ou 'sair'): ")
            if msg.lower() == "sair":
                break
            ssock.sendall(msg.encode())
            resposta = ssock.recv(1024)
            print(f"[🛡️] Resposta: {resposta.decode()}")