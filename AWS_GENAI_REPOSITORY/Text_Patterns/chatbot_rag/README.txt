# Chatbot with RAG

We will build a chatbot supported by Retrieval-Augmented Generation (RAG). 
We'll use Anthropic Claude, Amazon Titan Embeddings, and Streamlit. 
We will use Amazon Bedrock's built-in tool use capabilities to allow Anthropic Claude to decide when to use the retrieval-augmented generation pattern.

## Use Case
The chatbot with RAG pattern is good for the following use cases:

	- Simple interactive user conversation, supported by specialized knowledge or data

## Architecture 
- Past interactions are tracked in the chat memory object.
- The user enters a new message.
- The chat history is retrieved from the memory object and added before the new message.
- The question is converted to a vector using Amazon Titan Embeddings, then matched to the closest vectors in the vector database.
- The combined history, knowledge, and new message are sent to the model.
- The model's response is displayed to the user.

