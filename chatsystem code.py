from datetime import datetime

# -------------------------------
# Message Class
# -------------------------------
class Message:
    message_counter = 1  

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        return f"[{self.timestamp}] ({self.id}) {self.sender.username}: {self.content}"


# -------------------------------
# User Class
# -------------------------------
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom is not None:
            print(f"{self.username} is already in a chatroom.")
            return
        
        chatroom.add_user(self)
        self.chatroom = chatroom
        print(f"🔵 {self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if self.chatroom is None:
            print(f"{self.username} is not in any chatroom.")
            return
        
        print(f"🔴 {self.username} left {self.chatroom.name}")
        self.chatroom.remove_user(self)
        self.chatroom = None

    def send_message(self, content):
        if self.chatroom is None:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)


# -------------------------------
# ChatRoom Class
# -------------------------------
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        if user in self.users:
            print(f"{user.username} is already in {self.name}")
        else:
            self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)

    def show_chat_history(self):
        print(f"\n📜 Chat History of {self.name}:")
        if not self.messages:
            print("(No messages yet)\n")
            return
        
        for msg in self.messages:
            print(msg)
        print()


# ---------------------------------------
# Example Usage
# ---------------------------------------
if __name__ == "__main__":
    room = ChatRoom("Python Lounge")

    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello everyone!")
    u2.send_message("Hi Alice!")

    u3.join_chatroom(room)
    u3.send_message("Hey guys, what's up?")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()
