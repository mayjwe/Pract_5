import socket

HOST = input("Нажмите Enter, чтобы использовать локальный хост: ") or socket.gethostname()
PORT = 12345
import socket


def main():
    client = socket.socket()
    client.connect((HOST, PORT))
    while True:
        message = input("Введите сообщение (или 'exit' для выхода): ")
        client.send(message.encode('utf-8'))
        if message == 'exit':
            break

    client.close()


if __name__ == "__main__":
    main()
