import socket
import threading

HOST = socket.gethostname()
PORT = 12345
def exit(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message == 'exit':
            print("Клиент вышел")
            break
        print(f"Сообщение: {message}")
    client_socket.close()


def main():
    server = socket.socket()
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Сервер запущен на {HOST}:{PORT}, ожидаем подключения...")

    while True:
        client_socket, addr = server.accept()
        print(f"Подключен {addr}")
        client_handler = threading.Thread(target=exit, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    main()

