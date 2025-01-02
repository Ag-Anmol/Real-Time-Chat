from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import eventlet
eventlet.monkey_patch()  # Monkey patching for WebSocket support

# Create Flask app and SocketIO instance
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins for now

# Store users and their socket IDs
users = {}

@app.route('/')
def index():
    return render_template('index.html')  # Render the frontend page

# Handle WebSocket connection
@socketio.on('connect')
def handle_connect():
    print('Client connected:', request.sid)

# Handle user joining the chat
@socketio.on('join')
def handle_join(username):
    if username:
        users[request.sid] = username
        print(f'{username} has joined the chat')
        emit('message', {'sender': 'Server', 'message': f"{username} has joined the chat!"}, broadcast=True)

# Handle sending a message (group chat - no recipient needed)
@socketio.on('send_message')
def handle_send_message(message_data):
    try:
        sender = message_data.get('sender')
        message = message_data.get('message')

        if not sender or not message:
            raise ValueError("Sender and message must be provided.")

        print(f"Received message from {sender}: {message}")
        
        # Broadcast the message to all users in the group (no recipient needed)
        emit('receive_message', message_data, broadcast=True)

    except ValueError as ve:
        print(f"ValueError: {ve}")
        emit('error', {'message': str(ve)})
    except Exception as e:
        print(f"Error during message handling: {e}")
        emit('error', {'message': 'Error sending message'})

# Handle user disconnecting
@socketio.on('disconnect')
def handle_disconnect():
    username = users.pop(request.sid, None)
    if username:
        print(f'{username} has left the chat')
        emit('message', {'sender': 'Server', 'message': f"{username} has left the chat."}, broadcast=True)

# Run the Flask app with SocketIO support
if __name__ == '__main__':
    socketio.run(app, debug=True)
