from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app)

rooms_messages = {}
users_in_rooms = {}

@app.route('/')
def index():
    return render_template('index.html')

# Handle user joining a room
@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = data['room']
    
    # Join the room
    join_room(room)
    
    # Keep track of users in rooms
    if room not in users_in_rooms:
        users_in_rooms[room] = []
    if username not in users_in_rooms[room]:
        users_in_rooms[room].append(username)

    # Emit the user list to the room
    emit('user_list', users_in_rooms[room], room=room)
    
    # Emit previously sent messages of the room
    if room in rooms_messages:
        for message in rooms_messages[room]:
            emit('receive_message', {'sender': message[0], 'message': message[1], 'room': room}, room=room)

# Handle sending a message
@socketio.on('send_message')
def handle_message(data):
    sender = data['sender']
    message = data['message']
    room = data['room']
    
    if sender and message:  # Check that sender and message are not empty
        # Store message for the room
        if room not in rooms_messages:
            rooms_messages[room] = []
        rooms_messages[room].append((sender, message))
        
        # Broadcast the message to the room
        emit('receive_message', {'sender': sender, 'message': message, 'room': room}, room=room)
    else:
        print("Error: Message or sender is undefined.")

# Get list of recently visited rooms for a user
@socketio.on('get_recent_rooms')
def handle_get_recent_rooms(username):
    # Here we can use some storage to keep track of rooms the user has visited
    recent_rooms = []
    for room, users in users_in_rooms.items():
        if username in users:
            recent_rooms.append(room)
    emit('recent_rooms', recent_rooms)

# Get messages of a specific room
@socketio.on('get_messages')
def handle_get_messages(data):
    room = data['room']
    messages = rooms_messages.get(room, [])
    emit('receive_message', {'messages': messages, 'room': room})

# Handle user disconnecting from the room
@socketio.on('disconnect')
def handle_disconnect():
    for room, users in users_in_rooms.items():
        if username in users:
            users.remove(username)
            emit('user_list', users, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
