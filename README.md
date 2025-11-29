# Chat System (Python OOP Project)

A simple console-based chatroom system implemented in Python using Object-Oriented Programming.
This project demonstrates the use of classes, objects, message handling, user management, and chatroom broadcasting.

-------------------------
FEATURES
-------------------------

USER SYSTEM
- Users can join a chatroom
- Users can leave a chatroom
- Users can send messages

MESSAGING
Each message includes:
- Sender name
- Message ID
- Timestamp
(All messages are stored and displayed in chat history)

CHATROOM
- Multiple users can connect
- Broadcasts messages to all users
- Maintains chat history
- Prevents duplicate joins

-------------------------
PROJECT STRUCTURE
-------------------------

chat-system/
    chatsystem code.py   (Main Python script)
    README.md            (Documentation)

-------------------------
HOW TO RUN
-------------------------

1. Install Python (version 3.9+)
   Command:
   python --version

2. Run the script
   Command:
   python "chatsystem code.py"

-------------------------
CONCEPTS USED
-------------------------

- Classes & Objects
- Encapsulation
- Class variables
- Broadcasting messages
- Timestamps
- Clean OOP architecture

-------------------------
SAMPLE OUTPUT
-------------------------

Alice joined Python Lounge
Bob joined Python Lounge
[16:11:32] (1) Alice: Hello everyone!
[16:11:32] (2) Bob: Hi Alice!
Charlie joined Python Lounge
[16:11:32] (3) Charlie: Hey guys, what's up?

Chat History of Python Lounge:
[16:11:32] (1) Alice: Hello everyone!
[16:11:32] (2) Bob: Hi Alice!
[16:11:32] (3) Charlie: Hey guys, what's up?

Alice left Python Lounge
Bob left Python Lounge
Charlie left Python Lounge

-------------------------
FUTURE ENHANCEMENTS
-------------------------

- Multiple chatrooms
- Private messaging
- Tkinter GUI
- Web version (Flask / FastAPI)
- Chat logs saved to files
- Admin/moderator features

-------------------------
LICENSE
-------------------------

This project is open-source and free to use under the MIT License.
