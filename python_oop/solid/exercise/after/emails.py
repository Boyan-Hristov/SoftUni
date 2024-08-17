from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyMl(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class ISender(ABC):

    def __init__(self, sender: str):
        self.sender = sender

    @abstractmethod
    def format(self):
        pass


class IMSender(ISender):

    def format(self):
        return ''.join(["I'm ", self.sender])


class IReceiver(ABC):

    def __init__(self, receiver: str):
        self.receiver = receiver

    @abstractmethod
    def format(self):
        pass


class IMReceiver(IReceiver):

    def format(self):
        return ''.join(["I'm ", self.receiver])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: ISender):
        self.__sender = sender.format()

    def set_receiver(self, receiver: IMReceiver):
        self.__receiver = receiver.format()

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email('IM')
sender = IMSender("qmal")
email.set_sender(sender)
receiver = IMReceiver("james")
email.set_receiver(receiver)
content = MyMl("Hello, there!")
email.set_content(content)
print(email)
