import socket

def get_public_and_internal_ip():
    public_ip = socket.gethostbyname(socket.gethostname())
    internal_ip = socket.gethostbyname(socket.getfqdn())
    return public_ip, internal_ip
