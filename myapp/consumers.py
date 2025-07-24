

################### Chapter XVII topic 17.5: Forging the Real-time Link: Routing WebSockets and Creating Consumers ##################

import json
from channels.generic.websocket import WebsocketConsumer # For synchronous consumers

# EchoConsumer: A simple WebSocket consumer that echoes back any message it receives.
class EchoConsumer(WebsocketConsumer):
    # Called when a WebSocket connection is established.
    def connect(self):
        self.accept() # Accept the WebSocket connection
        print("WebSocket connected!") # Debugging: Confirm connection in server logs

    # Called when a message is received from the WebSocket.
    def receive(self, text_data):
        # Debugging: Print the raw incoming text data
        print(f"Received raw message: {text_data}")

        # Parse the incoming JSON message
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get('message', 'No message key found') # Use .get() for safer access
            print(f"Parsed message: {message}") # Debugging: Confirm parsed message
        except json.JSONDecodeError:
            message = f"Error: Received non-JSON data: {text_data}"
            print(message) # Log JSON decode error
            self.send(text_data=json.dumps({'error': message})) # Send error back to client
            return # Stop processing if JSON is invalid

        # Send the received message back to the client
        self.send(text_data=json.dumps({
            'message': message + " (echoed by server)" # Add a little note
        }))

    # Called when the WebSocket connection is closed.
    def disconnect(self, close_code):
        print(f"WebSocket disconnected with code: {close_code}") # Debugging: Confirm disconnect
        pass # No specific action needed on disconnect for this simple example
