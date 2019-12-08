import asyncio

class ClientError(Exception):
    pass


class ClientServerProtocol(asyncio.Protocol):
    list = {}

    def __init__(self):
        pass

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        lst = message.split()


        if (lst[0] == "put"):
            if not self.list:
                self.list[lst[1]] = [(lst[2], lst[3])]
            if lst[1] in self.list:
                if (lst[2], lst[3]) in self.list[lst[1]]:
                    pass
                else:
                    self.list[lst[1]].append((lst[2], lst[3]))
            else:
                self.list[lst[1]] = [(lst[2], lst[3])]
            self.transport.write('ok\n\n'.encode())
            return
        if (lst[0] == 'get'):
            if (lst[1] == '*'):
                ansv = 'ok\n'
                for i in self.list:
                    try:
                        if (self.list[i]):
                            self.list[i] = (sorted(self.list[i], key=lambda val: val[1]))
                            mass = self.list[i]
                            for m in mass:
                                ansv = ansv + i + ' ' + m[0] + ' ' + m[1] + '\n'
                        else:
                            self.transport.write('ok\n\n'.encode())
                    except ClientError:
                        self.transport.write("error\nwrong command\n\n".encode())
                ansv = ansv + '\n'
                self.transport.write(ansv.encode())

            else:
                try:
                    ansv = 'ok\n'
                    if lst[1] in self.list:
                        self.list[lst[1]] = (sorted(self.list[lst[1]], key=lambda val: val[1]))
                        mass = self.list[lst[1]]
                        for m in mass:
                            ansv = ansv + lst[1] + ' ' + m[0] + ' ' + m[1] + '\n'
                        ansv = ansv + '\n'
                        self.transport.write(ansv.encode())
                    else:
                        self.transport.write('ok\n\n'.encode())
                except ClientError:
                    self.transport.write("error\nwrong command1\n\n".encode())
            return
        self.transport.write("error\nwrong command1\n\n".encode())

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

