class Email():

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


email_objects = []
command = input()
while command != "Stop":
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    email_objects.append(email)
    command = input()

indices = [int(number) for number in input().split(", ")]
for index in indices:
    email_objects[index].send()

for email in email_objects:
    print(email.get_info())
