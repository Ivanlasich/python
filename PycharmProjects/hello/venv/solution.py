import asyncio


async def handle_echo(reader, writer):
    list = {}
    print(reader)
    data = await reader.read(1024)
    message = data.decode()
    lst = message.replace('.', '').split()
#    addr = writer.get_extra_info("peername")
    if(lst[0]=='put'):
        if not list:
            list[lst[1]]=[(lst[2], lst[3])]
        else:
            list[lst[1]].append((lst[2], lst[3]))
        print(list)
    writer.close()


loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, "127.0.0.1", 8181, loop=loop)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()