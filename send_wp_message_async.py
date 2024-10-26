import pywhatkit as kit
import datetime
import time

def send_whatsapp_message(phone_number, message, hour, minute):
    # Check if the time is in the future
    now = datetime.datetime.now()
    if (hour < now.hour) or (hour == now.hour and minute <= now.minute):
        print("The specified time is in the past. Please set a future time.")
        return

    # Schedule the message to be sent
    kit.sendwhatmsg(phone_number, message, hour, minute)

# Example usage
send_whatsapp_message("+919723888430", "Hello from Python!!", 11, 53)
