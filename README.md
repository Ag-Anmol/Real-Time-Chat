# Real-Time Chat Application

This project implements a real-time chat application using Flask and Flask-SocketIO. It enables users to join and create chat rooms, send and receive messages in real time, and view the list of active users in each room.

## Features

- Real-time messaging between users
- Ability to join or create chat rooms
- Display of active users in each room
- Persistence of messages within rooms
- User session management

## Technologies Used

- **Flask**: Web framework for Python
- **Flask-SocketIO**: WebSocket integration for real-time communication
- **Python**: Backend logic and state management
- **HTML, CSS**: Basic frontend for user interaction

## Requirements

- Python 3.x
- Flask
- Flask-SocketIO

To install dependencies, run:

```bash
pip install flask flask-socketio
```

## Running the Application

Start the Flask application with the following command:

```bash
python app.py
```
The server will run locally at `http://127.0.0.1:5000/`.

## Screenshots

### 1. Login Screen
![Login Screen](https://github.com/user-attachments/assets/c301236e-5b59-46ec-8154-f6931b3664ea)

### 2. Room Selection Screen
![Room Selection Screen](https://github.com/user-attachments/assets/a0bedf03-80e2-4eb8-8d75-9cc6602158ba)

### 3. Chat Window
![Chat Window](https://github.com/user-attachments/assets/5aa01e57-2420-4b70-a353-65413194810c)



## Skills Demonstrated in API Building

### 1. WebSocket Integration for Real-Time Communication
- Utilizes **Flask-SocketIO** to establish WebSocket connections, enabling real-time, bidirectional communication between clients and the server.
- Custom events are defined for managing user interactions, including joining rooms, sending messages, and updating active users.

### 2. API Design and Event Handling
- Custom **SocketIO events** handle various actions, such as joining a room (`join`), sending a message (`send_message`), and retrieving room-specific messages (`get_messages`).
- The backend uses event-driven architecture to respond to user actions promptly, ensuring low-latency interactions.

### 3. State Management
- **Persistent Room Data**: Messages and user lists are managed in memory, allowing the server to remember previous interactions and provide consistent data to clients.
- **Room-based Messaging**: Messages are stored per room, ensuring users in the same room can access all messages exchanged during the session.

### 4. User Management
- The application tracks users currently in each room. As users join or leave, the user list is updated in real time for all active users in that room.
- Upon joining a room, users are sent a history of previously exchanged messages, ensuring a seamless experience.

### 5. Session Management
- User sessions are managed in-memory for the duration of the chat. Active rooms and participants are dynamically updated.
- The server emits updates to all clients in real time when users join, leave, or send messages, ensuring that all participants are synchronized.

