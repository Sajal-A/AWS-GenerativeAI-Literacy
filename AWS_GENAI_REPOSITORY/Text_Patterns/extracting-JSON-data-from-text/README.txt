# Extracting JSON data from text

- We will build a JSON generator using Amazon Bedrock and Streamlit.

- Text to JSON allows us to extract hierarchical data from unstructured content. 
For example, we can extract information from a customer's email, including any referenced products, 
employees mentioned, sentiment, account numbers, and anything else the model can detect based on our prompt.

- We generate JSON through Amazon Bedrock's built-in tool use capabilities, which generate JSON responses based 
on a predefined JSON schema.

- The text to JSON pattern is good for the following use cases:
	- Email data extraction
	- Call transcript data extraction
	- Document data extraction

