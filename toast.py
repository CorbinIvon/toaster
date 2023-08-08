import sys
import socket
from plyer import notification
from time import sleep

class _conf_:
  # Default config
  port = 7515
  delimiter = "<|>"
  name="<use-dns>"
  def __init__(self):
    config_file = open("toast.conf", "r")
    for line in config_file:
      if line.startswith("port="):
        self.port = int(line[5:])
      elif line.startswith("delimiter="):
        self.delimiter = line[10:].strip()
      elif line.startswith("name="):
        display_name = line[5:].strip()
        if display_name != "\"\"":
          self.name = display_name
    config_file.close()
config=_conf_()

def send_notification(title, message):
  notification.notify(
    title=title,
    message=message,
    app_name="toaster",
    timeout=10  # Notification duration in seconds
  )

def listen():
  print("Listening for notifications...")
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(('0.0.0.0', config.port))
  s.listen(5)
  
  while True:
    client, addr = s.accept()
    data = client.recv(1024).decode('utf-8')
    sender, title, message = data.split(config.delimiter)
    if sender == "<use-dns>" or sender == "":
      sender=socket.gethostbyaddr(addr[0])[0]
    if sender == addr[0]:
      sender = addr[0]
    print(f"Received notification from {sender} ({addr[0]}:{addr[1]})")
    if not data:
      break
    send_notification(title, f"From: {sender}\n" + message)
    client.close()

def send(target_ip, title, message):
  print("Sending notification...")
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((target_ip, config.port))
  s.send(f"{config.name}{config.delimiter}{title}{config.delimiter}{message}".encode('utf-8'))
  s.close()

# If arg is --help or -h, print help
if len(sys.argv) > 1 and (sys.argv[1] == "--help" or sys.argv[1] == "-h"):
  print("Usage: python3 toast.py [OPTION]")
  print("Options:")
  print("  -l | --listen\tListen for notifications - No args")
  print("  -s | --send\tSend a notification - Args: [target_ip] [title] [message]")
  print("  -h | --help\tPrint this help message - No args")

# If arg is --listen, listen for notifications
elif len(sys.argv) > 1 and sys.argv[1] == "--listen" or sys.argv[1] == "-l":
  listen()

# If arg is --send, send a notification to device
elif len(sys.argv) > 3 and (sys.argv[1] == "--send" or sys.argv[1] == "-s"):
  send(sys.argv[2], sys.argv[3], sys.argv[4])

# If arg is --debug, print debug info
elif len(sys.argv) > 1 and sys.argv[1] == "--debug":
  print("Args:")
  for arg in sys.argv:
    print("  " + arg)
  print("Config:")
  print("  Port: " + str(config.port))
  print("  Delimiter: " + config.delimiter)
  print("  Name: " + config.name)