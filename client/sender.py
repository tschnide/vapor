import socket
import time


class Sender:

    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()

    port = 9999

    def __init__(self, files, reciever):
       self.files = files
       self.reciever = reciever

