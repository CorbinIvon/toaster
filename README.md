# toaster
Or is this a pager?
The toaster allows sending notifications to users on the same network!

# Features
1. Send notifications to devices on your local network.
2. Broadcast to all devices.
3. Receive notifications.

# To Do
- [x] Listen (server)
- [x] Send (client)
  - [x] Send to single
  - [ ] Send to multiple
- [ ] Background Listen
- [ ] GUI
- [ ] Tray Icon (Windows)

# Dependencies
```pip
pip install pyinstaller plyer
```

# Compile
```py
pyinstaller toast.spec
```
