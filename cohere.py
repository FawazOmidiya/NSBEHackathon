import cohere
# initialize the Cohere Client with an API Key
co = cohere.Client('ER2h4O9Vjk4gdTx0S1bYRttHGQIucPvpTwDWrg4r')

# generate a prediction for a prompt
prediction = co.chat(message='Help Lines for suicides in toronto', model='command')

# print the predicted text
print(f'Chatbot: {prediction.text}')