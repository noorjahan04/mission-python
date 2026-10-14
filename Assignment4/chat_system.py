# Q10. Concept: OOP (Object-Oriented Programming)
# Mini Project – OOP Chat System
# Create a Chat System using OOP concepts.
# Create the following classes:
# 1. User
# 2. Message
# 3. ChatRoom
#
# Implement the following functions:
# 1. Sending messages
# 2. Viewing chat history
# 3. User joining the chatroom
# 4. User leaving the chatroom


# Class 1: User
class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, chatroom, text):
        chatroom.send_message(self, text)

    def join_chatroom(self, chatroom):
        chatroom.join(self)

    def leave_chatroom(self, chatroom):
        chatroom.leave(self)


# Class 2: Message
class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def display_message(self):
        print(self.sender.name + ":", self.text)


# Class 3: ChatRoom
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    # User joins the chatroom
    def join(self, user):
        if user not in self.users:
            self.users.append(user)
            print(user.name, "joined", self.room_name)
        else:
            print(user.name, "is already in the chatroom")

    # User leaves the chatroom
    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            print(user.name, "left", self.room_name)
        else:
            print(user.name, "is not in the chatroom")

    # Send a message
    def send_message(self, user, text):
        if user in self.users:
            message = Message(user, text)
            self.messages.append(message)
            print("Message sent successfully")
        else:
            print("Please join the chatroom before sending messages")

    # View chat history
    def view_history(self):
        print("\nChat History:", self.room_name)

        if not self.messages:
            print("No messages yet")
        else:
            for message in self.messages:
                message.display_message()


# Create users
user1 = User("Noor")
user2 = User("Ayesha")

# Create a chatroom
room = ChatRoom("Python Group")

# Users join the chatroom
user1.join_chatroom(room)
user2.join_chatroom(room)

# Send messages
user1.send_message(room, "Hello everyone!")
user2.send_message(room, "Hi Noor!")
user1.send_message(room, "Welcome to the Python group.")

# View chat history
room.view_history()

# User leaves the chatroom
user2.leave_chatroom(room)

# Try sending a message after leaving
user2.send_message(room, "I am back!")

# View chat history again
room.view_history()