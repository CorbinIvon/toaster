from plyer import notification

def send_notification(title, message):
  notification.notify(
    title=title,
    message=message,
    app_name="MyApp",
    timeout=10  # Notification duration in seconds
  )

# Example usage:
send_notification("Hello", "This is a test notification!")