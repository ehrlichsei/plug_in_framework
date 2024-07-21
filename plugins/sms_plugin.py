# sms_plugin.py
from .message_plugin import MessagePlugin

class SMSPlugin(MessagePlugin):
    def send(self, message: str, recipient: str):
        print(f"Sending SMS to {recipient}: {message}")