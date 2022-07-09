import socket


SERVER_HOST_NAME = "localhost"
SERVER_PORT = 8000
DEFAULT_RESPONSE = "HTTP/1.1 200 OK\n\n"


def get_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST_NAME, SERVER_PORT))

    return server_socket


def get_method_and_path_from_request(request):
    all_info_from_request = request.split(" ")
    method = all_info_from_request[0][2:]
    path = all_info_from_request[1]

    return [method, path]


def main():
    server_socket = get_server_socket()
    server_socket.listen()

    while True:
        client_socket, address = server_socket.accept()
        request = client_socket.recv(1024)

        method, path = get_method_and_path_from_request(str(request))
        response = DEFAULT_RESPONSE + f"request method: {method}, request path: {path}"

        client_socket.sendall(response.encode())
        client_socket.close()


if __name__ == "__main__":
    main()
