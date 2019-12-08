import time
import socket


class ClientError(Exception):
    pass


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def put(self, key, val, timestamp=str(int(time.time()))):
        try:
            sock = socket.create_connection((self.host, self.port), self.timeout)
            sock.sendall(f"put {key} {val} {timestamp}\n".encode())
            dat = sock.recv(1024)
            dat = dat.decode()

            if (dat == 'error\nwrong command\n\n'):
                raise ClientError

        except ClientError:
            print("error")

    def get(self, key):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            sock.sendall(f"get {key}\n".encode())

            dat = sock.recv(1024)
            dat = dat.decode()
            data = {}
            if (dat):
                if (dat == 'ok\n\n'):
                    return data
                else:
                    mass = dat.split("\n")
                    for j in range(1, len(mass) - 2):
                        mass2 = mass[j].split(" ")
                        if mass2[0] in data:
                            data[mass2[0]] =data[mass2[0]] + ([(int(mass2[2]), float(mass2[1]))])
                        else:
                            if(mass2[2] and mass2[1]):
                                data[mass2[0]] = [(int(mass2[2]), float(mass2[1]))]
                return data
            else:
                raise ClientError