import sys, socket, struct
from plyer import notification

# Creator: Corbin Meier.
# Purpose: So I can send my wife, who is in the other room, the Minecraft IP and Port without opening up anything else because those are wasted seconds waiting for other large things to load when I need something simple and sweet OMG Discord needs to load faster.

class _conf_:
  # Default config
  port = 7515
  delimiter = "<|>"
  name="<use-dns>"
  interface="eth0"
  subnet="192.168.1.0
  def __init__(self):
    # If file exists, read config from file
    config_file = None
    try:
      config_file = open("toast.conf", "r")
    except FileNotFoundError:
      # Create config
      config_file = open("toast.conf", "w")
      config_file.write("port=7515\n")
      config_file.write("delimiter=\"<|>\"\n")
      config_file.write("name=\n")
      config_file.write("interface=\n")
      config_file.write("subnet=192.168.1.0\n")
      config_file.close()
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
      elif line.startswith("interface="):
        self.interface = line[10:].strip()
      elif line.startswith("subnet="):
        self.interface = line[7:].strip()
    config_file.close()
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
  s.settimeout(3)
  try:
    while True:
      try:
        client, addr = s.accept()
        data = client.recv(1024).decode('utf-8')
        sender, title, message = data.split(config.delimiter)
        if sender == "<use-dns>" or sender == "":
          sender = socket.gethostbyaddr(addr[0])[0]
        if sender == addr[0]:
          sender = addr[0]
        print(f"Received notification from {sender} ({addr[0]}:{addr[1]})")
        if not data:
          break
        send_notification(title, f"From: {sender}\n" + message)
        client.close()
      except socket.timeout:
        continue
  except KeyboardInterrupt:
    print("\nStopping the listener...")
    s.close()
def send(target_ip, title, message):
  print("Sending notification...")
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(4)
  try:
    s.connect((target_ip, config.port))
    s.send(f"{config.name}{config.delimiter}{title}{config.delimiter}{message}".encode('utf-8'))
  except socket.timeout:
    print("Connection refused. Is the target device running the listener?")
  s.close()
config=_conf_()
try:
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
  elif len(sys.argv) > 1 and sys.argv[1] == "--discover":
    # Find all devices on the network running the listener
    # Get subnet. This is hardcoded for now
    subnet = config.subnet
    # Use the config.interface to get the subnet
    subnet = ip_address[:ip_address.rfind(".")]
    # Loop through all IP addresses in subnet
    print (f"Scanning subnet " + subnet + ".0/24 on " + config.interface + "...")
    for i in range(1, 255):
      # Run a simple ping scan. Get hostname and IP address of all devices that respond
      hostname = None
      try:
        hostname = socket.gethostbyaddr(f"{subnet}.{i}")[0]
      except socket.herror:
        hostname = "Unknown"
        continue
      except socket.timeout:
        continue
      print(f"{subnet}.{i} ({hostname})")

  else:
    print("Invalid arguments. Use -h or --help for help.")
except KeyboardInterrupt:
  print("\nInterrupted by user. Exiting...")
  sys.exit(0)
