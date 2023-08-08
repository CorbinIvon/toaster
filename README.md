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
- [ ] Background Listener
  - Keep it running in the background.
- [ ] GUI
  - Allow the user to select 1 or more users to page.
- [ ] Tray Icon (Windows)
  - Used to quickly access and page users.

# Dependencies
```pip
pip install pyinstaller plyer
```

# Compile
```py
pyinstaller toast.spec
```
