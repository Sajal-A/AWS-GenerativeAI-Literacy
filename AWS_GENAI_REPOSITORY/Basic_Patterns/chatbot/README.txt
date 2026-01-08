# Chat bot

LLMs don't have any concept of state or memory. Any chat history has to be tracked externally and then passed into the model with each new message. 
We are using a list of custom objects to track chat history. Since there is a limit on the amount of content that can be processed by the model, 
we need to prune the chat history so there is enough space left to handle the user's message and the model's responses. 
Our code will delete older messages.

## Use Cases
- The chatbot pattern is good for the following use cases:

	- Simple interactive user conversation, without the use of any specialised knowledge or data.

## Architecture Overview
- Past interactions are tracked in the chat memory object.
- The user enters a new message.
- The chat history is retrieved from the memory object and added before the new message.
- The combined history & new message are sent to the model.
- The model's response is displayed to the user.

