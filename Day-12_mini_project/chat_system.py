class User :
    def __init__(self, username) :
        self.username = username
        
class Message :
    def __init__(self, sender, text) :
        self.sender = sender
        self.text = text

class ChatRoom :
    def __init__(self) :
        self.users = []
        self.messages = []

    def join(self, user) :
        self.users.append(user)

    def leave(self, user) :
        if user in self.users :
            self.users.remove(user)

    def send_message(self, user, text) :
        if (user in self.users) :
            msg = Message(user, text)
            self.messages.append(msg)
        else :
            print("User not in chat room")
    
    def show_messages(self) :
        for msg in self.messages :
            print(msg.sender.username, ":", msg.text)

u1 = User("Rahul")
u2 = User("Aman")

chat = ChatRoom()

chat.join(u1)
chat.join(u2)

chat.send_message(u1, "Hello")
chat.send_message(u2, "Hi bro")

chat.show_messages()

chat.leave(u1)
chat.send_message(u1, "Hi")
chat.show_messages()