from abc import ABC, abstractmethod


class Notification(ABC):

    def __init__(self, recipient: str):
        self.recipient = recipient

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def __init__(self, recipient: str, mail: str):
        super().__init__(recipient)
        self.mail = mail

    def send(self, message: str):
        print(f"Имэил отправлен: {self.recipient} на почту: {self.mail} с сообщением {message}")


class SMSNotification(Notification):
    def __init__(self, recipient: str, telephone: str):
        super().__init__(recipient)
        self.telephone = telephone

    def send(self, message: str):
        print(f"Сообщение отправлено: {self.recipient} на номер телефона: {self.telephone} с сообщением {message}")


class PushNotification(Notification):
    def __init__(self, recipient: str, app: str):
        super().__init__(recipient)
        self.app = app

    def send(self, message: str):
        print(f"Пуш уведомление отправлено: {self.recipient} в приложение: {self.app} с сообщением {message}")


notifications = [
    EmailNotification("Alex", "Alex@gmail.com"),
    SMSNotification("Анна", "+375291234567"),
    PushNotification("Олег", "Telegram"), ]

for notification in notifications:
    notification.send("гагага")