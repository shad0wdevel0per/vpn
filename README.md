# 🔐 VPN Educacional com Python + SSL

Este projeto demonstra como criar uma VPN educacional simples usando Python com criptografia SSL. É uma VPN conceitual que usa `socket` e `ssl` para simular um túnel seguro entre cliente e servidor, ideal para aprendizado sobre tunelamento e segurança de rede.

## 📌 Funcionalidades

- Túnel de comunicação criptografado com SSL
- Conexão segura ponto a ponto
- Exemplo prático de cliente-servidor em Python
- Ideal para estudos de VPN e redes seguras

## 📦 Requisitos

- Python 3
- Biblioteca `ssl` (já vem com Python)
- Certificados SSL (gerados com OpenSSL)

## 🔧 Como usar

### 1. Gere um certificado para o servidor:
```bash
openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem
```

---

### 📁 Projeto 2: `vpn_tun` (VPN Real com Interface TUN e Criptografia AES)

```markdown
# 🌐 VPN Real com Python (TUN + Criptografia AES)
```

Este projeto implementa uma VPN funcional em Python, usando interfaces TUN para tunelamento IP real e criptografia AES para segurança. É executado em sistemas Linux com suporte ao dispositivo `/dev/net/tun`.

## 🔐 Funcionalidades

- Túnel de rede real (camada IP)
- Interface TUN virtual (`tun0`)
- Criptografia AES-256 (modo EAX)
- Encaminhamento de pacotes IP entre cliente e servidor
- Comunicação segura via UDP

## ⚙️ Requisitos

- Linux com suporte a `/dev/net/tun`
- Acesso root (para configurar a interface)
- Python 3
- Biblioteca `pycryptodome`:
```bash
pip install pycryptodome

```bash
sudo python3 vpn_server.py
sudo python3 vpn_client.py
ping 10.8.0.1
```
