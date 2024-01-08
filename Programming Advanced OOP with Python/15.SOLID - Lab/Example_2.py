from abc import ABC, abstractmethod


class MessageService(ABC):
    @abstractmethod
    def send_message(self):
        pass


class Email(MessageService):
    def __init__(self, provider):
        self.provider = provider

    def send_message(self):
        return "sending email"


class SMS(MessageService):
    def send_message(self):
        return "sending sms"


class Slack(MessageService):
    def send_message(self):
        return "send message slack"


class Telegram(MessageService):
    def send_message(self):
        return "sending message in telegram"


class Notification:
    def __init__(self, service: MessageService):
        self._service = service

    def promotional_notification(self):
        self._service.send_message()


email = Email("gmail")
n = Notification(email)
n1 = Notification(Telegram())
