# Multimodal Chatbot
- We will build a multimodal chatbot with Amazon Bedrock, Anthropic Claude 3, and Streamlit.

- A multimodal chatbot is a chatbot that can understand text, images, and other formats. 
We will keep this example simple and stick to just text and images. We can upload or add some pre-created images, 
and then discuss them with the Claude 3 large language model.

- LLMs don't have any concept of state or memory. Any chat history has to be tracked externally and then passed into 
the model with each new message. We are using a list of custom objects to track chat history. Since there is a limit on the amount of 
content that can be processed by the model, we need to prune the chat history so there is enough space left to handle the user's message and the model's responses. 
Our code will delete older messages.

In this example, we're building the chatbot using the Amazon Bedrock Converse API

- The multimodal chatbot pattern is good for the following use cases:

	- Simple interactive user conversation with image analysis
	- Image comparisons
