import socket


def is_connected() -> bool:
    try:
        host = socket.gethostbyname('www.wikipedia.org')
        socket.create_connection((host, 80), 2)
        return True
    except TimeoutError:
        return False
    except socket.gaierror:
        return False


def scan_network(self):
    pass


def connect_to_network(self, network):
    pass


def change_mode(self, mode):
    pass
