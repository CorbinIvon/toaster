# toaster
Or is this a pager?

The toaster allows sending notifications to users on the same network!

What is a toast notification?

A toast notification is a small, non-intrusive message or alert that appears temporarily on the screen to convey some information to the user. 

[[Read More]](https://learn.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/toast-notifications-overview)

# Features
1. Send notifications to devices on your local network.
2. Broadcast to all devices.
3. Receive notifications.

# Compile
Windows: Run the build.bat

Linux: Run the build.sh

When the build is complete, the executable will be in the dist folder.

You can utilize the scripts in Windows to start the listener and send notifications.

# Commands
Start listening with `./toaster -l`. From here, you can listen for messages.

Here I am receiving a message from localhost.

![image](https://github.com/CorbinIvon/toaster/assets/20233488/ca8a8c67-9aa0-4dbe-91b6-cb2f077f842a)

Send a message with the -s flag `./toaster -s <IP_OR_HOSTNAME> "Title" "Message"`

Below shows an image of sending the message.

![image](https://github.com/CorbinIvon/toaster/assets/20233488/a855d1f1-ddd5-4658-b5c6-6d218323846c)

Simply replace localhost with who should receive the message! Make sure they're listening!!!


# To Do
- [x] Listen (server)
- [x] Send (client)
  - [x] Send to single
  - [ ] Send to multiple
- [x] Background Listener
  - Keep it running in the background.
- [ ] GUI
  - Allow the user to select 1 or more users to page.
- [ ] Tray Icon (Windows)
  - Used to quickly access and page users.

# Dependencies
```pip
pip install pyinstaller plyer
```
