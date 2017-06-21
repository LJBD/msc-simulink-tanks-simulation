import logging
import trollius


class PrintHandler(logging.Handler):
    def emit(self, record):
        print(record)


@trollius.coroutine
def handle_echo(reader, writer):
    while True:
        data = yield trollius.From(reader.readline())
        message = data.decode()
        addr = writer.get_extra_info('peername')
        print("Received %r from %r" % (message, addr))

        print("Send: %r" % message)
        writer.write(message.encode())
        yield trollius.From(writer.drain())

        print("Close the client socket")
        writer.close()


h = PrintHandler()
logging.getLogger("trollius").addHandler(h)

loop = trollius.get_event_loop()
coro = trollius.start_server(handle_echo, '0.0.0.0', 4567, loop=loop)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
