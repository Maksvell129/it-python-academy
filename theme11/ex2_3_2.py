from abc import ABC, abstractmethod




class Notification(ABC):
    def __init__(self, recipient):
        self.recipient = recipient
        self.validate_recipient()

    @abstractmethod
    def send(self, message):
        raise NotImplementedError

    @abstractmethod
    def validate_recipient(self):
        raise NotImplementedError


class EmailNotification(Notification):
    def __init__(self, recipient, subject):
        super().__init__(recipient)
        self.subject = subject


    def validate_recipient(self):
        # валидация почти
        pass

    def send(self, message):
        print(f'[Email] Кому: {self.recipient} Тема: "{self.subject}" Текст: {message}')


class SMSNotification(Notification):
    def __init__(self, recipient):
        super().__init__(recipient)

    def validate_recipient(self):
        # валидация телефона
        pass

    def send(self, message):
        print(f'[SMS] Кому: {self.recipient} Текст: {message}')


class PushNotification(Notification):
    def __init__(self, recipient, app_name):
        super().__init__(recipient)
        self.app_name = app_name

    def validate_recipient(self):
        # валидация app_id
        pass

    def send(self, message):
        print(f'Push {self.app_name} Пользователю {self.recipient}: {message}')


notifications = [
    EmailNotification('user@example.com', subject='Подтверждение заказа'),
    SMSNotification('+375291234567'),
    PushNotification('user_42', app_name='MyBank')
]

for notification in notifications:
    notification.send('Успешно')
