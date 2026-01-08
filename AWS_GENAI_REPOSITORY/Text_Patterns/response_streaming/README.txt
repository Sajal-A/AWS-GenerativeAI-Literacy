# Response Streaming

- We will build a response streaming application using Amazon Bedrock and Streamlit.
- Streaming responses are useful when you want to start returning content immediately to the end user. 
You can display the output a few words at a time, instead of waiting for the entire response to be created.

- The response streaming pattern is good for the following use cases:

	- Situations where longer text will be generated, but you want to 
	keep the user engaged by beginning to return a response immediately.

# Architecture Overview

- From an architectural perspective, response streaming is similar to text-to-text. 
We just need to add a special handler to immediately process the streaming output as it is created.

- The streamed response is returned in chunks of JSON. You can then extract the returned text from 
each chunk to be displayed to the end user.

