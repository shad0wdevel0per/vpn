import os
import fcntl
import struct
import socket
from crypto_utils import decrypt, encrypt

TUNSETIFF = 0x400454ca
IFF_TUN = 0x0001
IFF_NO_PI = 0x1000

def tun_alloc(dev):
    tun = open('/dev/net/tun', 'r+b')
    ifr = struct.pack('16sH', dev.encode(), IFF_TUN | IFF_NO_PI)
    fcntl.ioctl(tun, TUNSETIFF, ifr)
    return tun

tun = tun_alloc('tun0')
os.system('ip addr add 10.8.0.2/24 dev tun0')
os.system('ip link set dev tun0 up')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SERVER = ('<IP_DO_SERVIDOR>', 5555)  # Troque pelo IP real

print("[🔐] Cliente VPN TUN iniciado")

sock.settimeout(0.1)

while True:
    try:
        packet = tun.read(2048)
        sock.sendto(encrypt(packet), SERVER)
    except:
        pass

    try:
        data, _ = sock.recvfrom(2048)
        packet = decrypt(data)
        tun.write(packet)
    except:
        pass