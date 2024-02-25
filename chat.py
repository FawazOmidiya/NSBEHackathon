import cohere


def cohere_chat_bot():
    # Initialize the chat history
    chat_history = []

    # Define the preamble
    preamble_override = "You are connecting homeless people of color to social workers in Toronto"

    print('Starting the chat. Type "quit" to end.\n')

    co = cohere.Client('ER2h4O9Vjk4gdTx0S1bYRttHGQIucPvpTwDWrg4r')

    while True: 
        
        # User message
        message = input("User: ")
        
        # Typing "quit" ends the conversation
        if message.lower() == 'quit':
            print("Ending chat.")
            break

        # Chatbot response
        # Chatbot response
        response = co.chat(model="command",
                           message=message,
                           preamble_override=preamble_override,
                           stream=True,
                           chat_history=chat_history,
                           documents=[
                               {"title": "Emergency", "contact":"If you need emergency shelter, call 311 or Central Intake at 416-338-4766 for assistance."}, 
                               {"title": "shelter", "mixed": "101 Placer Ct"},
                               {"title": "shelter", "mixed": "1322 Bloor St W"},
                               {"title": "shelter", "women": "1st Stop Woodlawn Residence"},
                               {"title": "shelter",  "men": "705 Progress Ave Shelter Building E"},  
                               {"title": "shelter", "mixed": "4117 Lawrence Ave E Scarborough ON M1E 2S2"},
                               {"title": "shelter", "women": "67 Adelaide St E Toronto ON M5C 1K6"},
                               {"title": "shelter", "mixed": "545 Lake Shore Blvd W Toronto ON M5V 1A3"} 
                            ])
        
        chatbot_response = ""
        print("AI Social Worker: ", end='')
        
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


if __name__ == '__main__':
    cohere_chat_bot()