import socket
import re
meta = r'( |,|!|:|1|2|3|4|5|6|7|8|9|0)'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost', 8080)
sock.bind(serverAddress)
sock.listen(1)


def Encrypt(data):
    res = ""
    words = re.split(meta, data)
    for word in words:
        res += "".join(word[len(word)::-1])
    return res


while True:
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    try:
        print('Подключён:', client_address)
        while True:
            data = connection.recv(512)
            data = data.decode('utf-8')

            if data:
                data = Encrypt(data)
                connection.sendall(data.encode())
            else:
                break
    except:
        connection.close()
