# Initialize the chat history
chat_history = []

# Define the preamble
preamble_override = "You are connecting homeless people of color to social workers"

print('Starting the chat. Type "quit" to end.\n')

while True:
    
    # User message
    message = input("User: ")
    
    # Typing "quit" ends the conversation
    if message.lower() == 'quit':
        print("Ending chat.")
        break

    # Chatbot response
    response = co.chat(message=message,
                        preamble_override=preamble_override,
                        stream=True,
                        chat_history=chat_history)
    
    chatbot_response = ""
    print("Chatbot: ", end='')
    
    for event in response:
        if event.event_type == "text-generation":
            print(event.text, end='')
            chatbot_response += event.text
    print("\n")
    
    # Add to chat history
    chat_history.extend(
        [{"role": "USER", "message": message},
         {"role": "CHATBOT", "message": chatbot_response}]
    )