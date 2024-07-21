# email_plugin.py
from .message_plugin import MessagePlugin

class EmailPlugin(MessagePlugin):
    def send(self, message: str, recipient: str):
        print(f"Sending email to {recipient}: {message}")

