# Converse API

- The Amazon Bedrock Converse API provides a consistent way to access large language models (LLMs) using Amazon Bedrock. 
It supports turn-based messages between the user and the generative AI model. It also provides a consistent format for tool definitions 
for the models that support tool use (aka "function calling").

**Why is the Converse API so important?**
- Previously, with the InvokeModel API, you needed to use different JSON request and response structures for each model provider. 
The Converse API allows us to use a single format for requests and responses across all large language models on Amazon Bedrock.

## We will walk through:
1. A basic call to the Converse API
2. Alternating user and assistant messages
	- We can use the Converse API to send a list of previous messages along with a new message to the LLM to continue the conversation.
	You must alternate between messages from the "user" and "assistant" roles. The last message in the list should be from the 
	"user" role, so that the LLM can respond it.
3. Including an image in a message
	- We'll load a local image file and add its bytes to an image content block. We follow Anthropic's vision prompting tips and preface
	our image with the label "imag 1", then follow the images with our request.
4. Setting a System prompt
	- You can set a system prompt to communicate basic instructions for the large language model outside of the normal conversation.
	 System prompts are generally used by the developer to define the tone and constraints for the conversation. 

5. Getting response metadata and token count
	- The Converse method also returns metadata about the API call.
	- For example:
		- The `stopReason` property tells us why the model completed the message. This can be useful for your application logic, error handling, or troubleshooting.
		- The `usage` property includes details about the input and output tokens. This can help you understand the charges for your API call.



